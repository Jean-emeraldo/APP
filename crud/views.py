from django.shortcuts import render, redirect
from .forms import PatientForm
from .models import Patient
import joblib
import os
from django.conf import settings
from django.contrib import messages


def predict_diabetes(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)

            # Charger le modèle ML
            model_path = os.path.join(settings.BASE_DIR, 'crud/ml_models/diabetes_model.pkl')

            if not os.path.exists(model_path):
                messages.error(request, "Le modèle de prédiction est introuvable.")
                return redirect('predict')

            try:
                model = joblib.load(model_path)
            except Exception as e:
                messages.error(request, f"Erreur lors du chargement du modèle : {e}")
                return redirect('predict')

            # Préparer les données pour la prédiction
            data = [[
                patient.pregnancies,
                patient.glucose,
                patient.blood_pressure,
                patient.skin_thickness,
                patient.insulin,
                patient.bmi,
                patient.diabetes_pedigree,
                patient.age
            ]]

            # Faire la prédiction
            try:
                prediction = model.predict(data)[0]
                patient.outcome = bool(prediction)
                patient.save()
            except Exception as e:
                messages.error(request, f"Erreur lors de la prédiction : {e}")
                return redirect('predict')

            return render(request, 'crud/result.html', {'patient': patient})

    else:
        form = PatientForm()

    return render(request, 'crud/form.html', {'form': form})
