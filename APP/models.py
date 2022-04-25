from django.db import models

# Create your models here.

class Tanulo(models.Model):
    class Meta:
        verbose_name = 'Tanulo'
        verbose_name_plural = 'Tanulok'

    azon = models.CharField(max_length = 11)
    nev = models.CharField(max_length = 25)
    
    pont = models.FloatField()
    A_eredmeny = models.BooleanField()
    B_eredmeny = models.BooleanField()
    C_eredmeny = models.BooleanField()

    def __str__(self):
        return f"{self.azon}: {self.nev}"

