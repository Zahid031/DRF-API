from django.db import models
from django.utils.deconstruct import deconstructible


TASK_STATUS=(
    ('PENDING', 'PENDING'),
    ('COMPLETED', 'COMPLETED')
)


@deconstructible
class Task(models.Model):
    created_on=models.DateTimeField(auto_now_add=True)
    completed_on=models.DateTimeField(blank=True, null=True)
    created_by=models.ForeignKey('users.Profile',null=True, on_delete=models.SET_NULL,related_name='created_task')
    completed_task=models.ForeignKey('users.Profile',null=True, on_delete=models.SET_NULL,related_name='completed_task')
    name=models.CharField(max_length=100)
    description=models.TextField(null=True, blank=True)
    status=models.CharField(
        max_length=10,
        choices=TASK_STATUS,
        default='PENDING'
    )

    def __str__(self):
        return f'{self.id} | {self.name}'

