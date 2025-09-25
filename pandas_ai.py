import requests
import os
from pandasai import SmartDataframe
from pandasai.llm import LLM

from main import df

# Used AI for this code here - Connector for pandas AI with deepseek using a fetch req
class DeepSeekLLM(LLM):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.deepseek.com/v1"
        self._temperature = 0.1
        self._max_tokens = 1000

    def call(self, prompt: str) -> str:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        
        payload = {
            "model": "deepseek-chat",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": self._temperature,
            "max_tokens": self._max_tokens
        }
        
        response = requests.post(f"{self.base_url}/chat/completions", 
                                 headers=headers, 
                                 json=payload)
        response.raise_for_status()
        
        return response.json()["choices"][0]["message"]["content"]

    @property
    def type(self) -> str:
        return "deepseek"
deepseek_llm = DeepSeekLLM(os.getenv('api_token'))
# End of AI code


smart_df = SmartDataframe(df, config={
    "llm": deepseek_llm
})

response = smart_df.chat("What is the avarage value of amount")

print(response)