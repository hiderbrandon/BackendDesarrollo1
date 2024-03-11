from rest_framework import generics
from .models import Obra
from .serializers import ObraSerializer

from rest_framework import status
from rest_framework.response import Response

class ObraListCreateView(generics.ListCreateAPIView):
    queryset = Obra.objects.all()
    serializer_class = ObraSerializer
    
    
class ObraDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Obra.objects.all()
    serializer_class = ObraSerializer
    
class AllObrasListView(generics.ListAPIView):
    queryset = Obra.objects.all()
    serializer_class = ObraSerializer
    
class ObraUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Obra.objects.all()
    serializer_class = ObraSerializer
    partial = True
    
    
class ObraDeleteView(generics.DestroyAPIView):
    queryset = Obra.objects.all()
    serializer_class = ObraSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("delete Obra"))