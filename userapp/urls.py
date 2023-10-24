from rest_framework import routers
from .views import ProfissionalDeSaudeViewSet, VacinaViewSet, ProfissionalSaudeEUSFViewset, HistoricoDeVacinasViewset, UnidadeSaudeFamiliarViewset, CuidadorViewset, CuidadorCriancaViewset, CriancaViewset, CrescimentoCriancaViewset, AgendamentoViewSet, EnderecoViewSet, ConsultaViewSet, MedicoViewSet, CriancaVacinaViewSet, DesenvolvimentoViewset, SinaisAlertaViewset, CuidadosEspeciaisViewset

router = routers.DefaultRouter()

router.register(r'crescimentoCrianca', CrescimentoCriancaViewset)
router.register(r'desenvolvimento', DesenvolvimentoViewset)
router.register(r'sinaisAlerta', SinaisAlertaViewset)
router.register(r'cuidadosEspeciais', CuidadosEspeciaisViewset)
router.register(r'Crianca', CriancaViewset)
router.register(r'cuidador', CuidadorViewset)
router.register(r'CuidadorCrianca', CuidadorCriancaViewset)
router.register(r'endereco', EnderecoViewSet)
router.register(r'profissional', ProfissionalDeSaudeViewSet)
router.register(r'unidadesaudefamiliar', UnidadeSaudeFamiliarViewset)
router.register(r'profissionalEUSF', ProfissionalSaudeEUSFViewset)
router.register(r'medico', MedicoViewSet)
router.register(r'consulta', ConsultaViewSet)
router.register(r'agendamento', AgendamentoViewSet)
router.register(r'vacina', VacinaViewSet)
router.register(r'historico', HistoricoDeVacinasViewset)
router.register(r'criancavacina', CriancaVacinaViewSet)

urlpatterns = router.urls