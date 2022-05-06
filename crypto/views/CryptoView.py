from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from crypto.models.Asset import Asset


class CryptoView(APIView):
    def get(self, request):
        name = request.GET.get('name', '')
        currency = request.GET.get('currency', '')
        if not name or not currency:
            return HttpResponse("Request does not contain all required query", status=400)
        response = Asset.get_daily_change(name, currency)
        status = 200
        if type(response) == str:
            status = 400
        return HttpResponse(response, status=status)
