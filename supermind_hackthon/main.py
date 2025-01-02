# Note: Replace **<YOUR_APPLICATION_TOKEN>** with your actual Application token


import requests
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()


BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "44677293-a72d-4079-bac4-cfbe5c98d2ec"
FLOW_ID = "d24a2cf0-3972-4759-8912-ba8b537a702b"
APPLICATION_TOKEN = "AstraCS:MdsvFQcqCUMeXBGtdgXmfiHY:8ea5a6f6f2ececb191c137695b834087b3a6c52a95f4a5eb1f607f584c0d7089"
ENDPOINT = "test" # You can set a specific endpoint name in the flow settings

# You can tweak the flow by adding a tweaks dictionary
# e.g {"OpenAI-XXXXX": {"model_name": "gpt-4"}}


def run_flow(message: str) -> dict:
   
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"

    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }
   
    headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

def main():
    st.title("Chat Interface")
    
    message = st.text_area("Message", placeholder="Ask something...")
    
    if st.button("Run Flow"):
        if not message.strip():
            st.error("Please enter a message")
            return
    
        try:
            with st.spinner("Running flow..."):
                response = run_flow(message)
            
            response = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
            st.markdown(response)
        except Exception as e:
            st.error(str(e))

if __name__ == "__main__":
    main()


