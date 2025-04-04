from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistrationSerializer
from .models import PropertyInfo
from .serializers import PropertyInfoSerializer

class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Registration successful",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PropertyInfoListAPI(APIView):
    def get(self, request):
        data = PropertyInfo.objects.all()
        serializer = PropertyInfoSerializer(data, many=True)
        return Response(serializer.data)
