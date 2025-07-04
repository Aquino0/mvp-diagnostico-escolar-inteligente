# test_modelos.py

from model.modelo import Model
from model import Carregador, Avaliador

# Instanciação das Classes
carregador = Carregador()
modelo = Model()
avaliador = Avaliador()

# Parâmetros    
url_dados = "./MachineLearning/data/dados_treinamento.csv"
colunas = ['StudentID', 'Age', 'Gender', 'Ethnicity', 'ParentalEducation', 
           'StudyTimeWeekly', 'Absences', 'Tutoring', 'ParentalSupport',
           'Extracurricular', 'Sports', 'Music', 'Volunteering', 'GPA', 'GradeClass']

# Carga dos dados
dataset = carregador.carregar_dados(url_dados, colunas)

# Ajuste: supondo que 'GradeClass' já é binária (0 ou 1)
X = dataset.drop(columns=['StudentID', 'GradeClass', 'GPA'])
y = dataset['GradeClass']

def test_modelo_svm():
    """Testa se o modelo SVM tem acurácia maior que 0.7"""
    svm_path = './MachineLearning/models/modelo_svm_aprovacao_reprovacao.pkl'
    model_instance = Model()
    modelo_svm = model_instance.carrega_modelo(svm_path)
    
    # Avalia o modelo (supondo que avaliador.avaliar retorna acurácia)
    acuracia_svm = avaliador.avaliar(modelo_svm, X, y)
    print(f"Acurácia do modelo SVM: {acuracia_svm:.2%}")
    assert acuracia_svm > 0.7

# Se quiser adicionar mais testes (ex: testar rotas da API), veja exemplo abaixo
"""
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_alunos(client):
    response = client.get('/alunos')
    assert response.status_code in [200, 404]
"""
