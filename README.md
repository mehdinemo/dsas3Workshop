# Social Network Data Crawling Workshop

## Prerequisites

### Software Requirements
- Python 3.8 or higher
- pip (Python package manager)
- Git (version control)
- Virtual environment (venv or conda)

### Required Libraries
- tweepy
- snscrape
- telethon
- pyrogram
- python-dotenv
- spacy
- nltk
- transformers
- torch

## Setup Instructions

### 1. Create Virtual Environment
```bash
python3 -m venv workshop_env
source workshop_env/bin/activate  # On Windows, use `workshop_env\Scripts\activate`
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 3. API Credentials
Create a `.env` file in your project root with the following structure:
```
# Twitter API Credentials
TWITTER_CONSUMER_KEY=your_consumer_key
TWITTER_CONSUMER_SECRET=your_consumer_secret
TWITTER_ACCESS_TOKEN=your_access_token
TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret

# Telegram API Credentials
TELEGRAM_API_ID=your_api_id
TELEGRAM_API_HASH=your_api_hash
TELEGRAM_PHONE_NUMBER=your_phone_number
```

### 4. Obtaining API Credentials

#### Twitter Developer Account
1. Visit [Twitter Developer Portal](https://developer.twitter.com/)
2. Apply for a developer account
3. Create a new Project and App
4. Generate necessary API keys and tokens

#### Telegram API
1. Visit [Telegram API website](https://my.telegram.org/auth)
2. Log in with your Telegram account
3. Navigate to API development tools
4. Create a new application to obtain API ID and Hash

## Ethical Considerations
- Respect platform terms of service
- Obtain necessary permissions
- Protect user privacy
- Anonymize collected data
- Comply with data protection regulations

## Troubleshooting
- Ensure all dependencies are correctly installed
- Check API credentials
- Monitor rate limits
- Handle potential network and authentication errors

## Additional Resources
- [Tweepy Documentation](https://docs.tweepy.org/)
- [Telethon Documentation](https://docs.telethon.dev/)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/)
- [SpaCy NLP Library](https://spacy.io/usage)
