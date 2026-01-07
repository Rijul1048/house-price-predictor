import joblib
from django.shortcuts import render

model = joblib.load('../ml/house_price_model.pkl')

def home(request):
    prediction = None

    if request.method == 'POST':
        area = float(request.POST['area'])
        bedrooms = int(request.POST['bedrooms'])
        bathrooms = int(request.POST['bathrooms'])

        prediction = model.predict([[area, bedrooms, bathrooms]])[0]

    return render(request, 'home.html', {'prediction': prediction})
