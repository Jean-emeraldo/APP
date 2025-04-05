from django.db import models

class Patient(models.Model):
    name = models.CharField("Nom", max_length=100)
    age = models.IntegerField("Âge")
    pregnancies = models.IntegerField("Grossesses")
    glucose = models.FloatField("Taux de glucose")
    blood_pressure = models.FloatField("Pression artérielle")
    skin_thickness = models.FloatField("Épaisseur de peau")
    insulin = models.FloatField("Insuline")
    bmi = models.FloatField("IMC")
    diabetes_pedigree = models.FloatField("Hérédité")
    outcome = models.BooleanField("Diabète", null=True, blank=True)
    created_at = models.DateTimeField("Créé le", auto_now_add=True)

    def __str__(self):
        return self.name
