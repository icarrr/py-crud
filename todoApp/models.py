from django.db import models

_ = lambda text: text

class Task(models.Model):
    # define status choices/options
    class TaskStatus(models.TextChoices):
        BACKLOG = 'backlog', _('Backlog')
        TODO = 'todo', _('To Do')
        IN_PROGRESS = 'in_progress', _('In Progress')
        COMPLETED = 'closed', _('Completed')
    
    # define columns
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=TaskStatus.choices,
        default=TaskStatus.TODO
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # define table name
        db_table = 'tasks'
