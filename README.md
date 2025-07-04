
# Diagnóstico Escolar Inteligente

## 👨‍🎓 Sobre o Projeto

O **Diagnóstico Escolar Inteligente** é uma aplicação web que utiliza inteligência artificial para prever rapidamente se um aluno tem perfil para **aprovação ou reprovação** com base em dados escolares e comportamentais.

Este projeto foi desenvolvido como MVP para a disciplina de Segurança de Sistemas da PUC RIO, integrando técnicas de **Machine Learning**, backend com **Flask**, frontend web responsivo, banco de dados e testes automatizados.

---

## 🚀 Funcionalidades

- **Predição de aprovação/reprovação** de alunos via formulário web intuitivo
- Treinamento do modelo de machine learning com dados reais
- Integração full stack: Google Colab + Flask + Frontend HTML/CSS/JS
- Banco de dados SQLite para persistência dos alunos cadastrados
- **Resultado exibido de forma clara:** "Aprovado" ou "Reprovado"
- Testes automatizados com PyTest para garantir a robustez do modelo
- Documentação completa e vídeo explicativo

---

## 🖥️ Tecnologias Utilizadas

- **Frontend:** HTML5, CSS3 (Grid Layout), JavaScript
- **Backend:** Python 3, Flask, Flask-CORS, Flask-SQLAlchemy, flask-openapi3
- **Machine Learning:** Scikit-learn, Pandas, Numpy, Joblib
- **Banco de dados:** SQLite (SQLAlchemy ORM)
- **Testes:** PyTest
- **Modelagem/Notebook:** Google Colab

---

## 📊 Dataset

- **Fonte:** Kaggle: https://www.kaggle.com/datasets, processados em [dados_treinamento.csv](MachineLearning/data/dados_treinamento.csv)
- **Atributos principais:**  
  Nome, Idade, Gênero, Etnia, Educação dos Pais, Tempo de Estudo Semanal, Faltas, Apoio Escolar, Apoio dos Pais, Atividades Extracurriculares, Esportes, Música, Voluntariado, Resultado
- **Variável alvo:**  
  `GradeClass` (1 = Aprovado, 0 = Reprovado)

---

## 💡 Como Rodar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/SEU_USUARIO/diagnostico-escolar-inteligente.git
cd diagnostico-escolar-inteligente/api
```

### 2. Crie e ative um ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate  # (Mac/Linux)
venv\Scriptsctivate     # (Windows)
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Rode o backend Flask

```bash
python app.py
```

Acesse: [http://127.0.0.1:5000](http://127.0.0.1:5000) no navegador

---

### 5. (Opcional) Rodando os testes automatizados

```bash
pytest -v test_modelos.py
```

---

## 📒 Treinamento do Modelo

O modelo foi treinado e avaliado em um notebook Colab dedicado, com toda a pipeline de pré-processamento, modelagem, validação cruzada, seleção do melhor algoritmo, avaliação final e exportação do modelo `.pkl`.

- [Notebook no Google Colab](https://colab.research.google.com/drive/SEU_LINK_AQUI)
- Métricas principais:
    - **Acurácia:** (preencher valor)
    - **Precision, Recall, F1:** (preencher valores)
    - Gráficos de comparação de modelos e matriz de confusão incluídos no notebook.

---

## 📋 Exemplo de uso

1. Preencha o formulário com os dados do aluno
2. Clique em “Prever”
3. Veja imediatamente o resultado "Aprovado" ou "Reprovado" tanto no alerta quanto na tabela
4. O histórico dos alunos cadastrados aparece logo abaixo, podendo ser removido individualmente

---

## ✅ Testes Automatizados

- **Arquivo:** `test_modelos.py`
- **Principais testes:**
    - Acurácia mínima do modelo (assert > 0.7)
    - Rotas principais da API (GET, POST)
    - Robustez na adição e remoção de alunos
---

## 👤 Autor

Cristopher Aquino  
PUC RIO – Segurança de Sistemas – 2025.  
[LinkedIn](https://www.linkedin.com/in/cristopher-aquino-4992b251/) | [Email](cristopheraquino20@gmail.com)

---

## 📌 Checklist de entrega

- [x] Notebook Colab no repositório
- [x] Modelo `.pkl` treinado e salvo
- [x] Backend Flask rodando
- [x] Frontend moderno e responsivo
- [x] Testes PyTest funcionando
- [x] README completo
