# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor
from .models import Measurement
from .serializers import MeasurementSerializer, SensorDetailSerializer, SensorSerializer


class MeasurementView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class SensorsView(RetrieveUpdateAPIView, ListCreateAPIView):
    queryset = Sensor.objects.all()
    # serializer_class = SensorSerializer
    serializer_class = SensorDetailSerializer


# class SensorAdd(CreateAPIView):
class SensorAdd(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    # serializer_class = SensorDetailSerializer

    # def post(self, request):
    #     return Response({'status': 'OK'})
