# Sample Telegram Data Collection Simulation
from datetime import datetime
from enum import Enum
from typing import Optional, List

from pydantic import BaseModel


class MediaType(str, Enum):
    TEXT = "text"
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    LOCATION = "location"


class TelegramMessage(BaseModel):
    id: int
    sender: str
    text: str
    timestamp: datetime
    media_type: Optional[MediaType] = None
    reply_to: Optional[int] = None
    forward_from: Optional[str] = None
    location: Optional[str] = None
    entities: Optional[List[str]] = None


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
            timestamp="2024-02-15T10:30:45",
            media_type=MediaType.TEXT,
            entities=["#AIResearch", "natural language processing"]
        ),
        TelegramMessage(
            id=1002,
            sender="DataScientist_22",
            text="Check out this interesting visualization of machine learning trends.",
            timestamp="2024-02-15T11:15:20",
            media_type=MediaType.TEXT,
            reply_to=1001,
            forward_from="Tech_Insights_Channel"
        ),
        TelegramMessage(
            id=1003,
            sender="GlobalTechNews",
            text="Breaking: Major tech conference announces keynote speakers for upcoming AI summit.",
            timestamp="2024-02-15T12:45:10",
            media_type=MediaType.TEXT,
            entities=["AI summit", "tech conference"],
            forward_from="TechCrunch"
        ),
        TelegramMessage(
            id=1004,
            sender="ResearchMethodology",
            text="Important thread on ethical considerations in data collection 🔍\n\n1/3 Privacy is paramount\n2/3 Consent matters\n3/3 Anonymization is crucial",
            timestamp="2024-02-15T14:20:30",
            media_type=MediaType.TEXT,
            entities=["data collection", "ethical considerations"]
        ),
        TelegramMessage(
            id=1005,
            sender="CodersNetwork",
            text="Python 3.12 released with significant performance improvements! Checkout the new features.",
            timestamp="2024-02-15T15:55:00",
            media_type=MediaType.TEXT,
            entities=["Python", "programming"],
            reply_to=None
        ),
        TelegramMessage(
            id=1006,
            sender="AIEthicsDiscussion",
            text="Debate: Can large language models truly understand context?\n\nPerspectives from leading researchers:\n- Dr. Emily Chen argues for nuanced interpretation\n- Prof. Michael Rodriguez emphasizes computational limitations",
            timestamp="2024-02-15T16:40:15",
            media_type=MediaType.TEXT,
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


def main():
    # Example usage
    telegram_data = generate_sample_telegram_data()
    data_analysis = analyze_telegram_data(telegram_data)

    print("Telegram Data Analysis:")
    for key, value in data_analysis.items():
        print(f"{key.replace('_', ' ').title()}: {value}")


if __name__ == "__main__":
    main()
