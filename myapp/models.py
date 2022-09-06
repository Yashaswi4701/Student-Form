from django.db import models

# Create your models here.
class Contacts(models.Model):
    name=models.CharField(max_length=30)
    usn=models.CharField(max_length=10)
    email=models.EmailField(max_length=80)
   
    
    def __str__(self):
        return f"{self.name} is a student with USN {self.usn}"