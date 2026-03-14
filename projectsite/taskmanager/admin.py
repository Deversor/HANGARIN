from django.contrib import admin
from .models import Priority, Category, Task, SubTask, Note

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "deadline", "priority", "category")
    list_filter = ("status", "priority", "category")
    search_fields = ("title", "description")

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "get_parent_task")
    list_filter = ("status",)
    search_fields = ("title", "parent_task__title")

    def get_parent_task(self, obj):
        return obj.parent_task.title
    get_parent_task.short_description = 'Parent Task'

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("task", "content", "created_at")
    list_filter = ("created_at",)
    search_fields = ("content",)

admin.site.register(Category)
admin.site.register(Priority)