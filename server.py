""" Executing this function initiates the application of EMOTION
    DETECTION to be executed over the Flask channel and deployed on
    localhost:5000.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def emo_detector():
    ''' This FUNTION receives the text from the HTML interface and 
        runs EMOTION DETECTION over it using emotion_detector() function.
        The output returned shows the emotionsl and the dominant emotion 
        for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    try:
        status_code = response['status_code']
        if response['dominant_emotion'] is None:
            return "Invalid text! Please try again!"
    except ValueError as e:
        print(f"ValueError occurred: {e}")
    except TypeError as e:
        print(f"TypeError occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    if response and status_code == 200:
        try:
            response.pop('status_code', None)
        except:
            pass

        anger = response['anger']
        disgust = response['disgust']
        fear = response['fear']
        joy =response['joy']
        sadness = response['sadness']
        dom = response['dominant_emotion']

        return (f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
                f"'joy': {joy}, 'sadness': {sadness}. The dominant emotion is <b>{dom}</b>."
        )
    return f"The text provided is invalid. Status code = {status_code}"

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)
