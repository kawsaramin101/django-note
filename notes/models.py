import uuid
from django.db import models
from django.contrib.auth.models import User



class Note(models.Model):
    
    secondary_id = models.UUIDField(default=uuid.uuid4, unique=True)
    creator = models.ForeignKey(User, related_name="notes", on_delete=models.CASCADE, null=False, blank=False)
    title = models.CharField(max_length=2000, null=True, blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]
    
    def __str__(self):
        return str(self.id)
        

class NoteEditHistory(models.Model):

    secondary_id = models.UUIDField(default=uuid.uuid4, unique=True)
    edited_instance = models.ForeignKey(Note, related_name="previous_versions", on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=2000)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ["-created"]
    
    def __str__(self):
        return str(self.id)
        
