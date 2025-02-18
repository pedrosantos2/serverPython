import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_API_URL = os.getenv("BASE_API_URL")
ENDPOINT_FJ = os.getenv("ENDPOINT_FJ")
ENDPOINT_JSP = os.getenv("ENDPOINT_JSP")

def run_flow_jsp(message: str) -> dict:
    api_url = f"{BASE_API_URL}/api/v1/run/{ENDPOINT_JSP}"
    payload = {
        "input_value": message, 
        "output_type": "chat",
        "input_type": "chat"
    }
    headers = {"Content-Type": "application/json"}   
    response = requests.post(api_url, json=payload, headers=headers)
  
    return response.json()

def jsp_tool_func(query: str) -> str:
    """
    Processa o comando /rtJSP utilizando o fluxo do LangFlow,
    retornando somente o conteúdo do campo 'message' do array 'messages'.
    """
    if query.lower().startswith("/rtjsp"):
        query = query[6:].strip()
    if not query:
        return "Por favor, forneça uma entrada válida após /rtFJ."
    
    try:
        flow_response = run_flow_jsp(query)
        
        result_text = flow_response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
        
        if not result_text:
            return "Erro: Nenhuma resposta gerada pelo fluxo."
        
        return result_text
      
    except Exception as e:
        print(f"Erro no pipeline JSP: {e}")
        return f"Erro interno: {e}"

def run_flow_fj(message: str) -> dict:
    api_url = f"{BASE_API_URL}/api/v1/run/{ENDPOINT_FJ}"
    payload = {
        "input_value": message, 
        "output_type": "chat",
        "input_type": "chat"
    }
    headers = {"Content-Type": "application/json"}   
    response = requests.post(api_url, json=payload, headers=headers)
  
    return response.json()

def fj_tool_func(query: str) -> str:
    """
    Processa o comando /rtFJ utilizando o fluxo do LangFlow,
    retornando somente o conteúdo do campo 'message' do array 'messages'.
    """
    if query.lower().startswith("/rtfj"):
        query = query[5:].strip()
    if not query:
        return "Por favor, forneça uma entrada válida após /rtFJ."
    
    try:
        flow_response = run_flow_fj(query)
        
        result_text = flow_response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
        
        if not result_text:
            return "Erro: Nenhuma resposta gerada pelo fluxo."
        
        return result_text
      
    except Exception as e:
        print(f"Erro no pipeline FJ: {e}")
        return f"Erro interno: {e}"


def process_user_query(query: dict) -> str:
    """
    Processa a entrada do usuário.
    """
    user_input = query.get("user_input", "").strip()
    if not user_input:
        return "Por favor, digite alguma coisa."
    
    try:
        if user_input.lower().startswith("/rtjsp"):
            return jsp_tool_func(user_input)
        if user_input.lower().startswith("/rtfj"):
            return fj_tool_func(user_input)

    except Exception as e:
        print(f"Erro geral ao processar a solicitação: {e}")
        return "Erro ao processar sua solicitação."
