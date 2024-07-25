''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : TODO
# Import the sentiment_analyzer function from the package created: TODO
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
#Initiate the flask app : TODO
app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyzer function and store the response
    result = emotion_detector(text_to_analyze)
    # Extract the label and score from the response

    # Check if the label is None, indicating an error or invalid input
    if result is None:
        return "Invalid input! Try again."
    else:
        # Return a formatted string with the sentiment label and score
        return (f"For the given statement, the system response is 'anger': {result['anger']}, "
              f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and "
              f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}.")
@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    ''' 
    app.run(host="0.0.0.0", port=5000)
