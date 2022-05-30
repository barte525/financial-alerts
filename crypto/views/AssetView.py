from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from crypto.models.Asset import Asset
from django.http import JsonResponse
from crypto.models.consts import main_currencies


class AssetView(APIView):
    def get(self, request):
        name = request.GET.get('name', '')
        currency = request.GET.get('currency', '')
        if not name or not currency:
            return HttpResponse("Request does not contain all required query", status=400)
        response = Asset().get_new_crypto_price(name, currency)
        status = 200
        if type(response) == str:
            status = 400
        return HttpResponse(response, status=status)


def get_all(request):
    assets = Asset.objects.all()
    assets_name = []
    for asset in assets:
        assets_name.append({
            'name': asset.name,
            'pricePLN': asset.converterPLN,
            'priceEUR': asset.converterEUR,
            'priceUSD': asset.converterUSD,
            'description': Asset().scrap_info(asset.name)
        })
    return JsonResponse(assets_name, safe=False)


def get_all_names(request):
    assets = Asset.objects.all()
    assets_name = []
    for asset in assets:
        assets_name.append({
            'name': asset.name,
        })
    return JsonResponse(assets_name, safe=False)

def get_detail(request):
    name = request.GET.get('name', '')
    if not name:
        return HttpResponse("Request does not contain all required query", status=400)
    if name not in Asset.objects.values_list('name', flat=True):
        return HttpResponse("Incorrect name", status=400)
    return JsonResponse({'detail': Asset().scrap_info(name)})


def get_currencies(request):
    currencies = []
    for currency in main_currencies:
        currencies.append({
           'currency': currency
        })
    return JsonResponse(currencies, safe=False)