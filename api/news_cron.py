import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import requests
import json

from prompt.gpt_api import generate_questions
  

def get_api_key():  
    # Opening JSON file
    with open('api/creds/cred.json') as f:
        data = json.load(f)

    api_key = data['apikey']
    # Closing file
    f.close()
    return api_key


def fetch_and_save():
    api_key = get_api_key()
    # Initialize the Firebase app with your service account credentials
    cred = credentials.Certificate('api/creds/newsai-379605-firebase-adminsdk-yoo87-5732267602.json')
    firebase_admin.initialize_app(cred)

    # Get a Firestore client instance
    db = firestore.client()

    # Define the Newsdata.io API endpoint URL
    url = 'https://newsdata.io/api/1/news'

    # Define the API parameters
    params = {
        'apikey': api_key,
        'language': 'en',  # the language of the news articles
        'country': 'in'
    }
    
    n = 0
    while n <=5 :
        # Send a GET request to the API endpoint with the parameters
        response = requests.get(url, params=params)
        # Check if the request was successful
        if response.status_code == 200:
            # Convert the response JSON data to a Python dictionary
            data = response.json()
            next = data["nextPage"]
            # Create a batch write instance
            batch = db.batch()
            print(f"saving batch num {n}")
            # Loop through each news article in the API response
            for article in data['results']:
                # Define a new document reference in Firestore with a generated ID
                doc_ref = db.collection('news_ai').document()
                # Add the set operation for the document to the batch
                content = article['content']
                ##TODOscale out later
                questions = generate_questions(content)
                print(questions)
                batch.set(doc_ref, {
                    'content': article['content'] or "content",
                    'description': article['description'] or "description",
                    'img_url': article['image_url'] or "url",
                    'pub_date': article['pubDate'] or "pub",
                    'src_link': article['link'] or "link",
                    'title': article['title'] or "title",
                    'category': article['category'],
                    'questions': questions
                })
            # Commit the batch write
            batch.commit()
        else:
            # Print an error message if the request was not successful
            print(f"Error: {response.status_code} - {response.reason}")
            break
        n +=1
        params["page"]=next