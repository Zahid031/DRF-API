from rest_framework import viewsets
from .serializers import HouseSerializer

from .permissions import IsHouseManagerOrNone
from .models import House

class HouseViewSet(viewsets.ModelViewSet):
    queryset=House.objects.all()
    permission_classes=[IsHouseManagerOrNone]
    serializer_class=HouseSerializer