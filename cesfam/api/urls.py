from rest_framework import routers
from .viewsets import *

router = routers.SimpleRouter()
router.register('atenciones-medicas', Atencion_MedicaViewSet)
router.register('carnet-pacientes', Carnet_PacienteViewSet)
router.register('detalle-atenciones', Detalle_AtencionViewSet)
router.register('detalle-recetas', Detalle_RecetaViewSet)
router.register('entregas', EntregaViewSet)
router.register('errores', ErrorViewSet)
router.register('estado-reservas', Estado_ReservaViewSet)
router.register('farmaceuticos', FarmaceuticoViewSet)
router.register('farmacias', FarmaciaViewSet)
router.register('medicamentos', MedicamentoViewSet)
router.register('medicos', MedicoViewSet)
router.register('pacientes', PacienteViewSet)
router.register('recetas-medicas', Receta_MedicaViewSet)
router.register('reposiciones', ReposicionViewSet)
router.register('reservas', ReservaViewSet)
router.register('retiros-stock', Retiro_StockViewSet)
router.register('stock', StockViewSet)
router.register('tipos-retiro', Tipo_RetiroViewSet)
router.register('usuarios', UsuarioViewSet)

urlpatterns = router.urls