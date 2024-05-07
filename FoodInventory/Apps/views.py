import requests
from django.shortcuts import render, redirect
from .forms import InputForm
from django.urls import reverse
from .models import Product

def index(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            upc = form.cleaned_data['upc']

            # Check if the UPC exists in the database
            try:
                product = Product.objects.get(upc=upc)
                ean = product.ean
                title = product.title
                brand = product.brand
                print("{}\t{}\t{}".format(ean, title, brand))
                print("found in DB!!!!")
            except Product.DoesNotExist:
                # Make a request to the API with the provided UPC
                headers = {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Accept-Encoding': 'gzip,deflate',
                }
                resp = requests.get(f'https://api.upcitemdb.com/prod/trial/lookup?upc={upc}', headers=headers)
                if resp.status_code == 200:
                    data = resp.json()
                    if 'items' in data:
                        first_item = data['items'][0]  # Get the first item from the list of items
                        ean = first_item.get('ean', '')
                        title = first_item.get('title', '')
                        brand = first_item.get('brand', '')
                        
                        # Add the product to the database
                        Product.objects.create(upc=upc, ean=ean, title=title, brand=brand)
                        
                        print("{}\t{}\t{}".format(ean, title, brand))
                    else:
                        print("No 'items' found in API response.")
                else:
                    print("Failed to retrieve data from the API. Status code:", resp.status_code)
            return redirect(reverse('index'))  # Redirect to a success page or render the result
    else:
        form = InputForm()

    return render(request, 'index.html', {'form': form})
