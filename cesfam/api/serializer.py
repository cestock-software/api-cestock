from .models import *
from rest_framework import serializers

class Atencion_MedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atencion_Medica
        fields = '__all__'

class Carnet_PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carnet_Paciente
        fields = '__all__'

class Detalle_AtencionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalle_Atencion
        fields = '__all__'

class Detalle_RecetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalle_Receta
        fields = '__all__'

class EntregaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrega
        fields = '__all__'

class ErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Error
        fields = '__all__'

class Estado_ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado_Reserva
        fields = '__all__'

class FarmaceuticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmaceutico
        fields = '__all__'

class FarmaciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmacia
        fields = '__all__'

class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = '__all__'

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class Receta_MedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receta_Medica
        fields = '__all__'

class ReposicionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reposicion
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

class Retiro_StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retiro_Stock
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

class Tipo_RetiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_Retiro
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'