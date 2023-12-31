from rest_framework import serializers
from .models import ProfissionalDeSaude, Vacina, ProfissionalSaudeEUSF, UnidadeSaudeFamiliar, HistoricoDeVacinas, Cuidador, CuidadorCrianca, Crianca, CrescimentoCrianca, Agendamento, Endereco, Consulta, Medico, CriancaVacina, Desenvolvimento, SinaisAlerta, CuidadosEspeciais

class CrescimentoCriancaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrescimentoCrianca
        fields = '__all__'

class DesenvolvimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desenvolvimento
        fields = '__all__'

class SinaisAlertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SinaisAlerta
        fields = '__all__'

class CuidadosEspeciaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuidadosEspeciais
        fields = '__all__'

class CriancaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crianca
        fields = '__all__'

class CuidadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuidador
        fields = '__all__'

class CuidadorCriancaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuidadorCrianca
        fields = '__all__'

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'

class ProfissionalDeSaudeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfissionalDeSaude
        fields = '__all__'

class UnidadeSaudeFamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadeSaudeFamiliar
        fields = '__all__'

class ProfissionalSaudeEUSFSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfissionalSaudeEUSF
        fields = '__all__'

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'

class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = '__all__'

class VacinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacina
        fields = '__all__'

class HistoricoDeVacinasSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoDeVacinas
        fields = '__all__'

class CriancaVacinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CriancaVacina
        fields = '__all__'