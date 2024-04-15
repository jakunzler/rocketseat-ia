from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn
import joblib

# Criar uma instância do FastAPI
app = FastAPI()

# Criar uma classe que terá os dados do request para a API
class RequestBody(BaseModel):
  horas_estudo : float
  
  
# Carregar modelo para realizar a predição
modelo_pontuacao = joblib.load('./modelo_regressao_linear.pkl')

@app.post('/predict')

def predict(data : RequestBody):
  # Preparar os dados para predição
  input_feature = [[data.horas_estudo]]
  
  # Realizar a predição
  y_pred = modelo_pontuacao.predict(input_feature)[0].astype(int)
  
  return {'pontuacao_teste' : y_pred.tolist()}