from django.core.management.base import BaseCommand
from faker import Faker
from django.utils import timezone
from taskmanager.models import Priority, Category, Task, SubTask, Note
import random

class Command(BaseCommand):
    help = 'Create initial data for Hangarin'

    def handle(self, *args, **kwargs):
        fake = Faker()
        
        # 1. Manual Creation
        p_list = ["High", "Medium", "Low", "Critical", "Optional"]
        c_list = ["Work", "School", "Personal", "Finance", "Projects"]
        
        priorities = [Priority.objects.get_or_create(name=name)[0] for name in p_list]
        categories = [Category.objects.get_or_create(name=name)[0] for name in c_list]

        # 2. Fake Tasks
        for _ in range(20):
            task = Task.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.paragraph(nb_sentences=3),
                deadline=timezone.make_aware(fake.date_time_this_month()),
                status=random.choice(["Pending", "In Progress", "Completed"]),
                category=random.choice(categories),
                priority=random.choice(priorities)
            )
            
            # Subtask
            SubTask.objects.create(
                parent_task=task,
                title=fake.sentence(nb_words=3),
                status=task.status
            )
            
            # Note
            Note.objects.create(task=task, content=fake.paragraph())

        self.stdout.write(self.style.SUCCESS('Hangarin data populated!'))