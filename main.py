from grant_proposal.proposal_helper import generate_proposal_outline
from chatbot.chatbot import CommunityChatbot
from content_creation.content_creator import create_educational_content
from volunteer_management.volunteer_scheduler import send_volunteer_invitation
from sentiment_analysis.sentiment_analyzer import analyze_feedback, visualize_sentiment

def main():
    # Example of generating a grant proposal outline
    print(generate_proposal_outline("Community Garden"))

    # Interaction with Community Chatbot
    chatbot = CommunityChatbot(api_key="YOUR_API_KEY")
    print(chatbot.get_response("Tell me about upcoming events."))

    # Create educational content
    print(create_educational_content("Recycling", "students"))

    # Sending a volunteer email
    send_volunteer_invitation("volunteer@example.com", "Environmental Cleanup on Oct 10")

    # Sentiment Analysis
    feedback = ["Great initiative!", "I love this project.", "Could be better."]
    analyses = [analyze_feedback(text) for text in feedback]
    visualize_sentiment(analyses)

if __name__ == "__main__":
    main()
