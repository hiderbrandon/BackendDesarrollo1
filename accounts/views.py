from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import get_object_or_404
from .serializers import MyTokenObtainPairSerializer, UserSerializer ,AllFieldsUserSerializer
from .models import CustomUser

from django.shortcuts import render
from .models import CustomUser
# Create your views here.

#Login User
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

#Register User
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

#api/profile  and api/profile/update
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProfile(request):
    user = request.user
    serializer = AllFieldsUserSerializer(user, many=False)  # Utiliza AllFieldsUserSerializer en lugar de UserSerializer
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateProfile(request):
    user = request.user
    serializer = AllFieldsUserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteProfile(request):
    user_id = request.data.get('user_id')  # Obtener la ID del usuario del cuerpo de la solicitud
    user = get_object_or_404(CustomUser, id=user_id)
    user.delete()
    return Response({"message": "User deleted successfully"})