from flask import Flask
import views


app = Flask(__name__)
app.debug = True

# Don't do this!
app.secret_key = "bacon"

app.add_url_rule('/', view_func=views.IndexView.as_view('index'),
                 methods=['GET', 'POST'])


# app.add_url_rule('/tweets', methods=['POST', 'GET'])
# def create_tweet():
#     if request.method == 'POST':
#         return jsonify(tweets.append({"text": request.form['tweet'],
#                                       "id": randint(0, 256)}))
#     else:
#         return jsonify({"tweets": tweets})


# @app.route('/tweets/<int:id>', methods=['GET', 'DELETE'])
# def single_tweet(id):
#     if request.method == 'GET':
#         # serve a tweet
#         for tweet in tweets:
#             if tweet.id == id:
#                 return jsonify(tweet)
#         return jsonify({})
#     else:
#         # delete a tweet
#         for tweet in tweets:
#             if tweet.id == id:
#                 tw = tweet
#                 tweets.remove(tw)
#                 return jsonify(tw)
#         return jsonify({})

if __name__ == "__main__":
    app.run()
