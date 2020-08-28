from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.


def HomePage(request):
    tags = ['Gust', 'Hotel', 'Devices']
    rating = 4
    return render(request, 'index.html', {'name': 'Board Data',
                                          'tags': tags,
                                          'rating': rating, })


def Home(request):
    return render(request, 'home.html')


def ControlDevice(request):
    return render(request, 'controller.html')


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)