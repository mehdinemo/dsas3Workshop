import os

import snscrape.modules.twitter as sntwitter
import spacy
import tweepy
from telethon.sync import TelegramClient
from transformers import pipeline


class SocialNetworkCrawler:
    def __init__(self):
        # Twitter Authentication
        self.twitter_consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
        self.twitter_consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
        self.twitter_access_token = os.getenv('TWITTER_ACCESS_TOKEN')
        self.twitter_access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

        # Telegram Authentication
        self.telegram_api_id = os.getenv('TELEGRAM_API_ID')
        self.telegram_api_hash = os.getenv('TELEGRAM_API_HASH')
        self.telegram_phone_number = os.getenv('TELEGRAM_PHONE_NUMBER')

        # Initialize NLP and ML models
        self.nlp = spacy.load('en_core_web_sm')
        self.sentiment_pipeline = pipeline('sentiment-analysis')

    def twitter_api_authentication(self):
        """Authenticate with Twitter API v2"""
        try:
            client = tweepy.Client(
                consumer_key=self.twitter_consumer_key,
                consumer_secret=self.twitter_consumer_secret,
                access_token=self.twitter_access_token,
                access_token_secret=self.twitter_access_token_secret
            )
            return client
        except Exception as e:
            print(f"Twitter API Authentication Error: {e}")
            return None

    def telegram_client_authentication(self):
        """Authenticate Telegram Client"""
        try:
            client = TelegramClient(
                self.telegram_phone_number,
                self.telegram_api_id,
                self.telegram_api_hash
            )
            client.start()
            return client
        except Exception as e:
            print(f"Telegram Client Authentication Error: {e}")
            return None

    def collect_twitter_data(self, query, max_results=100):
        """Collect Twitter data using multiple methods"""
        twitter_data = []

        # Method 1: Tweepy API
        twitter_client = self.twitter_api_authentication()
        if twitter_client:
            try:
                tweets = twitter_client.search_recent_tweets(query=query, max_results=max_results)
                twitter_data.extend(tweets.data)
            except Exception as e:
                print(f"Tweepy API Error: {e}")

        # Method 2: Snscrape (fallback method)
        try:
            for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
                if i >= max_results:
                    break
                twitter_data.append(tweet)
        except Exception as e:
            print(f"Snscrape Error: {e}")

        return twitter_data

    def collect_telegram_messages(self, channel_username, limit=100):
        """Collect messages from a Telegram channel"""
        telegram_messages = []

        with self.telegram_client_authentication() as client:
            try:
                for message in client.iter_messages(channel_username, limit=limit):
                    telegram_messages.append(message)
            except Exception as e:
                print(f"Telegram Message Collection Error: {e}")

        return telegram_messages

    def preprocess_text(self, text):
        """Preprocess and clean text data"""
        doc = self.nlp(text)
        cleaned_tokens = [
            token.lemma_.lower()
            for token in doc
            if not token.is_stop and not token.is_punct
        ]
        return ' '.join(cleaned_tokens)

    def analyze_sentiment(self, text):
        """Perform sentiment analysis using Hugging Face pipeline"""
        return self.sentiment_pipeline(text)[0]

    def generate_report(self, platform_data, platform_name):
        """Generate analysis report"""
        print(f"{platform_name} Data Analysis Report")
        print("-" * 40)

        sentiments = []
        for item in platform_data:
            text = item.text if platform_name == 'Twitter' else item.message
            preprocessed_text = self.preprocess_text(text)
            sentiment = self.analyze_sentiment(preprocessed_text)

            print(f"Text: {preprocessed_text[:100]}...")
            print(f"Sentiment: {sentiment['label']} (Score: {sentiment['score']})\n")
            sentiments.append(sentiment['label'])

        # Basic sentiment distribution
        sentiment_counts = {
            'POSITIVE': sentiments.count('POSITIVE'),
            'NEGATIVE': sentiments.count('NEGATIVE')
        }
        print("Sentiment Distribution:")
        print(sentiment_counts)


def main():
    crawler = SocialNetworkCrawler()

    # Twitter Data Collection
    twitter_query = "AI innovation"
    twitter_data = crawler.collect_twitter_data(twitter_query)
    crawler.generate_report(twitter_data, 'Twitter')

    # Telegram Data Collection
    telegram_channel = "some_telegram_channel"
    telegram_data = crawler.collect_telegram_messages(telegram_channel)
    crawler.generate_report(telegram_data, 'Telegram')


if __name__ == "__main__":
    main()
