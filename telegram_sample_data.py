# Sample Telegram Data Collection Simulation

class TelegramMessage:
    def __init__(self,
                 id,
                 sender,
                 text,
                 timestamp,
                 media_type=None,
                 reply_to=None,
                 forward_from=None,
                 entities=None):
        self.id = id
        self.sender = sender
        self.text = text
        self.timestamp = timestamp
        self.media_type = media_type
        self.reply_to = reply_to
        self.forward_from = forward_from
        self.entities = entities or []


def generate_sample_telegram_data():
    """
    Generate a realistic sample of Telegram messages demonstrating 
    various types of communication scenarios.
    """
    return [
        TelegramMessage(
            id=1001,
            sender="AI_Research_Group",
            text="Exciting breakthrough in natural language processing! Our new model shows 95% accuracy in sentiment analysis. 🚀 #AIResearch",
            timestamp="2024-02-15 10:30:45",
            media_type="text",
            entities=["#AIResearch", "natural language processing"],
            reply_to=None
        ),
        TelegramMessage(
            id=1002,
            sender="DataScientist_22",
            text="Check out this interesting visualization of machine learning trends.",
            timestamp="2024-02-15 11:15:20",
            media_type="image",
            reply_to=1001,
            forward_from="Tech_Insights_Channel"
        ),
        TelegramMessage(
            id=1003,
            sender="GlobalTechNews",
            text="Breaking: Major tech conference announces keynote speakers for upcoming AI summit.",
            timestamp="2024-02-15 12:45:10",
            media_type="text",
            entities=["AI summit", "tech conference"],
            forward_from="TechCrunch"
        ),
        TelegramMessage(
            id=1004,
            sender="ResearchMethodology",
            text="Important thread on ethical considerations in data collection 🔍\n\n1/3 Privacy is paramount\n2/3 Consent matters\n3/3 Anonymization is crucial",
            timestamp="2024-02-15 14:20:30",
            media_type="text",
            entities=["data collection", "ethical considerations"]
        ),
        TelegramMessage(
            id=1005,
            sender="CodersNetwork",
            text="Python 3.12 released with significant performance improvements! Checkout the new features.",
            timestamp="2024-02-15 15:55:00",
            media_type="text",
            entities=["Python", "programming"],
            reply_to=None
        ),
        TelegramMessage(
            id=1006,
            sender="AIEthicsDiscussion",
            text="Debate: Can large language models truly understand context?\n\nPerspectives from leading researchers:\n- Dr. Emily Chen argues for nuanced interpretation\n- Prof. Michael Rodriguez emphasizes computational limitations",
            timestamp="2024-02-15 16:40:15",
            media_type="text",
            entities=["AI ethics", "language models", "context understanding"],
            reply_to=None
        )
    ]


def analyze_telegram_data(messages):
    """
    Perform basic analysis on the crawled Telegram messages
    """
    analysis = {
        "total_messages": len(messages),
        "media_type_distribution": {},
        "top_senders": {},
        "message_with_entities": 0,
        "forwarded_messages": 0,
        "reply_messages": 0
    }

    for message in messages:
        # Media type distribution
        analysis["media_type_distribution"][message.media_type] = \
            analysis["media_type_distribution"].get(message.media_type, 0) + 1

        # Top senders
        analysis["top_senders"][message.sender] = \
            analysis["top_senders"].get(message.sender, 0) + 1

        # Entities and special message types
        if message.entities:
            analysis["message_with_entities"] += 1

        if message.forward_from:
            analysis["forwarded_messages"] += 1

        if message.reply_to:
            analysis["reply_messages"] += 1

    return analysis


# Example usage
telegram_data = generate_sample_telegram_data()
data_analysis = analyze_telegram_data(telegram_data)

print("Telegram Data Analysis:")
for key, value in data_analysis.items():
    print(f"{key.replace('_', ' ').title()}: {value}")
