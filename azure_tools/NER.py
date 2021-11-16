from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

key = "921242739dac433db87fc7edd6b719ca"
endpoint = "https://nzx.cognitiveservices.azure.com/"

def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint,
            credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

def entity_recognition_example(client):

    try:
        documents = ["The Indian-origin CEO of a pharmaceutical company was killed in a robbery attempt allegedly by a man who followed him all the way to his home from a casino after seeing him win nearly $10,000, according to media reports. Sree Ranga Aravapalli, 54, who headed Aurex Laboratories, was shot dead when he reached his home in Plainsboro, New Jersey, early Tuesday morning, officials said."]
        result = client.recognize_entities(documents = documents)[0]

        print("Named Entities:\n")
        for entity in result.entities:
            print("\tText: \t", entity.text, "\tCategory: \t", entity.category, "\tSubCategory: \t", entity.subcategory,
                    "\n\tConfidence Score: \t", round(entity.confidence_score, 2), "\tLength: \t", entity.length, "\tOffset: \t", entity.offset, "\n")

    except Exception as err:
        print("Encountered exception. {}".format(err))

entity_recognition_example(client)