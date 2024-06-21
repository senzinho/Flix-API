from django.db import models

#constantes / tuplas, só tem 1 valor igual
NATIONALITY_CHOICES = (
    ('US', 'Estados Unidos'),
    ('BR', 'Brasil'),
)

class Actor(models.Model):
    name = models.CharField(max_length=200)
    nationality = models.CharField(max_length=100, choices=NATIONALITY_CHOICES,blank=True,null=True)

    def __str__(self):
        return self.name