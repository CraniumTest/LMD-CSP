import openai

def create_educational_content(subject, target_audience):
    response = openai.Completion.create(
      engine="gpt-3.5-turbo",
      prompt=f"Create an educational article about {subject} for {target_audience}",
      max_tokens=500
    )
    
    return response.choices[0].text.strip()
