import openai

def generate_proposal_outline(topic, language_model="gpt-3.5-turbo"):
    openai.api_key = "YOUR_API_KEY"

    response = openai.Completion.create(
      engine=language_model,
      prompt=f"Create an outline for a grant proposal on {topic}",
      max_tokens=150
    )
    
    return response.choices[0].text.strip()
