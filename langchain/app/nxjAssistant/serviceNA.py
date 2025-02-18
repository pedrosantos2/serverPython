import requests
from dotenv import load_dotenv
import os

load_dotenv()

BASE_API_URL = os.getenv("BASE_API_URL")
ENDPOINT = "NXJAssistente" 

def run_flow(message: str) -> dict:
    """
    Run a flow with a given message and optional tweaks.

    :param message: The message to send to the flow
    :param endpoint: The ID or the endpoint name of the flow
    :param tweaks: Optional tweaks to customize the flow
    :return: The JSON response from the flow
    """
    api_url = f"{BASE_API_URL}/api/v1/run/{ENDPOINT}"

    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }
    headers = None
   
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()


def process_ask(query: str) -> str:
    """
    Process a user query using the LangFlow pipeline.

    :param query: The user query to process
    :return: The response from the pipeline
    """
    
    if query.lower().startswith("/nxj"):
        query = query[4:].strip()
    else:
        query = query
    
    try:
        flow_response = run_flow(query)
        result_text = flow_response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
        return result_text
    except Exception as e:
        print(f"Error in the pipeline: {e}")
        return f"Internal error: {e}"
