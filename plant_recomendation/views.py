# plant_recomendation/views.py
from django.shortcuts import render, redirect
from .forms import DataForm
# from .models import Data
import pickle


# Load Decision Tree model from .pickle file
with open('model/decision_tree_model.pickle', 'rb') as file:
    decision_tree_model = pickle.load(file)


def index(request):
    return render(request, 'dashboard/index.html')


def rekomendasi(request):
    prediction_result = None
    form = DataForm()

    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            data = [form.cleaned_data['temperature'],
                    form.cleaned_data['altitude']]
            prediction_result = decision_tree_model.predict([data])[0]
    return render(request, 'dashboard/rekomendasi.html', {'form': form, 'prediction_result': prediction_result})


def komoditas(request):
    return render(request, 'dashboard/komoditas.html')


def tentang(request):
    return render(request, 'dashboard/tentang.html')
