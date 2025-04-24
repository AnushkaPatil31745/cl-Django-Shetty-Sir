from django.db import models

class comments(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
   

    def __str__(self):
        return self.description

# Create your models here.


# comments : ['blog','description']