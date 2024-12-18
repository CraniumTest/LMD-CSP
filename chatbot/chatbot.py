import openai

class CommunityChatbot:
    def __init__(self, api_key, language_model="gpt-3.5-turbo"):
        openai.api_key = api_key
        self.language_model = language_model

    def get_response(self, query):
        response = openai.ChatCompletion.create(
          model=self.language_model,
          messages=[{"role": "user", "content": query}]
        )
        
        return response.choices[0].message['content'].strip()
