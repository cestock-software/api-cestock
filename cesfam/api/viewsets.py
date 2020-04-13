from rest_framework import viewsets
from .models import *
from .serializer import *

class Atencion_MedicaViewSet(viewsets.ModelViewSet):
    queryset = Atencion_Medica.objects.all()
    serializer_class = Atencion_MedicaSerializer

class Carnet_PacienteViewSet(viewsets.ModelViewSet):
    queryset = Carnet_Paciente.objects.all()
    serializer_class = Carnet_PacienteSerializer

class Detalle_AtencionViewSet(viewsets.ModelViewSet):
    queryset = Detalle_Atencion.objects.all()
    serializer_class = Detalle_AtencionSerializer

class Detalle_RecetaViewSet(viewsets.ModelViewSet):
    queryset = Detalle_Receta.objects.all()
    serializer_class = Detalle_RecetaSerializer

class EntregaViewSet(viewsets.ModelViewSet):
    queryset = Entrega.objects.all()
    serializer_class = EntregaSerializer

class ErrorViewSet(viewsets.ModelViewSet):
    queryset = Error.objects.all()
    serializer_class = ErrorSerializer

class Estado_ReservaViewSet(viewsets.ModelViewSet):
    queryset = Estado_Reserva.objects.all()
    serializer_class = Estado_ReservaSerializer

class FarmaceuticoViewSet(viewsets.ModelViewSet):
    queryset = Farmaceutico.objects.all()
    serializer_class = FarmaceuticoSerializer

class FarmaciaViewSet(viewsets.ModelViewSet):
    queryset = Farmacia.objects.all()
    serializer_class = FarmaciaSerializer

class MedicamentoViewSet(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class Receta_MedicaViewSet(viewsets.ModelViewSet):
    queryset = Receta_Medica.objects.all()
    serializer_class = Receta_MedicaSerializer

class ReposicionViewSet(viewsets.ModelViewSet):
    queryset = Reposicion.objects.all()
    serializer_class = ReposicionSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class Retiro_StockViewSet(viewsets.ModelViewSet):
    queryset = Retiro_Stock.objects.all()
    serializer_class = Retiro_StockSerializer

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class Tipo_RetiroViewSet(viewsets.ModelViewSet):
    queryset = Tipo_Retiro.objects.all()
    serializer_class = Tipo_RetiroSerializer
   
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer