from django.db import models

class Trainer(models.model):
    first_name = models.Charfield(max_length=30 null=False)
    last_name = models.Charfield(max_length=30 null=False)
    birth_date = models.DateField()
    level = models.IntegerField(default=1)
# Create your models here.
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Pokemon(models.Model):
    name = models.CharField(max_length=30, null=False)
    POKEMON_TYPES = {
        ('A', 'Agua'),
        ('F', 'Fuego'),
        ('T', 'Tierra'),
        ('P', 'Planta'),
        ('A', 'Electrico '),
        ('A', 'Lagartija'),
    }
    type = models.CharField(max_length=30, choices=POKEMON_TYPES, null=False)
    weight = models.DecimalField(max_digits= 6, decimal_places=4)
    height = models.DecimalField(max_digits= 6, decimal_places=4)
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null= True)
    picture = models.ImageField(upload_to="pokemon_images")
    def __str__(self):
        return self.name

