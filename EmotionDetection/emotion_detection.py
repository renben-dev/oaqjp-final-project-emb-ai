"""
    this module provide function emotion_detector(text_to_analyze).
    It returns:
        a python dictionary with keys:
            'label':
            'score':
            'status_code':
"""

import json
import requests

def emotion_detector(text_to_analyze):
    """
        Analyzes the emotion of the provided text using Watson's Emotion API.
        Parameters:
        text_to_analyze (str): The text whose emotion is to be analyzed.
        Returns:
        dictionary: 'anger', disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score, 'dominant_emotion': dominant_emotion
    """    
    url =   (
            'https://sn-watson-emotion.labs.skills.network/v1/'
            'watson.runtime.nlp.v1/NlpService/EmotionPredict'
            )
    headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}    
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = input_json, headers = headers, timeout = 60)
    dict_response =json.loads(response.text)
    status_code = response.status_code
    if status_code == 200:
        emotions = dict_response['emotionPredictions'][0]['emotion']

        anger_score = emotions['anger']
        disgust_score = emotions['disgust']
        fear_score = emotions['fear']
        joy_score = emotions['joy']
        sadness_score = emotions['sadness']        
        dominant_emotion = max(emotions, key=emotions.get)
    else:
        anger_score, disgust_score, fear_score, joy_score, sadness_score, dominant_emotion = None, None, None, None, None, None

    return  {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion
            }

        # dict_response =json.loads(response.text)
    # status_code = response.status_code
    # if status_code == 200:
    #     label = dict_response['documentSentiment']['label']
    #     score = dict_response['documentSentiment']['score']
    # else:
    #     label = None
    #     score = None
    # return {'label': label, 'score': score, 'status_code': status_code}


    # """
    #     Analyzes the emotion of the provided text using Watson's Emotion API.
    #     Parameters:
    #     text_to_analyze (str): The text whose emotion is to be analyzed.
    #     Returns:
    #     dict: A dictionary containing the emotion label ('label'), 
    #         emotion score ('score'), and the status code ('status_code') 
    #         of the API response.
    # """