from flask import Flask, request, jsonify
import tweepy

app = Flask(__name__)

# Twitter API keys
API_KEY = "gvdJfBZNxe7tcjzdqBcvydz1k"
API_SECRET = "6XseNKC9YKQegJSmFLLpSne4IFJsFPeA2pVVo6Vy8O1lZgQEAl"
ACCESS_TOKEN = "1897246085137227776-JUFTf13W7fHOGpgPIrBWoJPLXKzjLc"
ACCESS_TOKEN_SECRET = "Qi3sPWnz6Ni8uGKgwXTCn9qQpXLiZZa2QLl6bbtSJoe9W"

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

@app.route('/api/tweets', methods=['GET'])
def get_tweets():
    username = request.args.get('username')
    tweets = api.user_timeline(screen_name=username, count=5)
    tweet_texts = [tweet.text for tweet in tweets]
    return jsonify(tweet_texts)

if __name__ == "__main__":
    app.run(debug=True)
