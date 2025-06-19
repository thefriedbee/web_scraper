"""
Combine manually searching with playwright to scrape tweets

1. Manually login and choose the search query
2. Use playwright to scroll to the bottom of the page
    2.1 Scrape the tweets
    2.2 Save the tweets to a file
3. The program is a infinite loop. After scrolling for 100 times, user choose the next query or exit the program
"""
from playwright.sync_api import sync_playwright
import time


def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080}
        )
        page = context.new_page()
        # Go to the search page
        url_live = "https://x.com/search?q=nyc%20congestion%20pricing&src=typed_query&f=live"
        url_hot = "https://x.com/search?q=nyc%20congestion%20pricing&src=typed_query"
        page.goto(url_live)
        # login with username and password manually
        time.sleep(60)  # Wait for content to load; adjust as needed

        CONTINUE = True
        seen_tweets = set()
        while CONTINUE:
            # Scroll to load more tweets
            for _ in range(25):
                page.mouse.wheel(0, 540)
                time.sleep(3)
            
            # extract tweets and store them
            all_tweets = extract_tweets(page)
            new_tweets = []
            for tweet in all_tweets:
                # Use first 100 characters as unique identifier
                tweet_id = tweet[:100]
                if tweet_id not in seen_tweets:
                    seen_tweets.add(tweet_id)
                    new_tweets.append(tweet)
            
            print(f"Found {len(new_tweets)} new tweets.")
            if new_tweets:
                store_tweets(new_tweets)
            
            
            # Ask user if they want to continue
            # User can use the browser to search for the next query or exit the program
            user_input = input("Do you want to continue? (y/n): ")
            if user_input.lower() == "n":
                CONTINUE = False
    
        # exit the program
        browser.close()


def extract_tweets(page):
    tweets = page.locator("article").all()
    all_tweets = []
    for tweet in tweets:
        text = tweet.inner_text()
        all_tweets.append(text)
    return all_tweets


def store_tweets(tweets):
    with open("data/tweets_live.txt", "a+") as f:
        for tweet in tweets:
            f.write("--- New Tweet ---\n")
            f.write(tweet + "\n\n")


if __name__ == "__main__":
    run()

