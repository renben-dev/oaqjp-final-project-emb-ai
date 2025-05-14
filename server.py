from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def emo_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response and response['status_code'] == 200:
        try:
            response.pop('status_code', None)
        except:
            pass
        return response
    else:
        try:
            status_code = response['status_code']
        except:
            status_code = 500

        return f"The text provided is invalid. Status code = {status_code}"

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)