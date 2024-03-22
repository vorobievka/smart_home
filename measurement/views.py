# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView, ListCreateAPIView
from .serializers import MeasurementSerializer, SensorDetailSerializer, SensorSerializer
from .models import Sensor
from .models import Measurement


class MeasurementView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class SensorsView(RetrieveUpdateAPIView, ListCreateAPIView):
    queryset = Sensor.objects.all()

    def get_serializer_class(self):
        if self. request.method == 'GET':
            return SensorDetailSerializer
        else:
            return SensorSerializer


class SensorAdd(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer






