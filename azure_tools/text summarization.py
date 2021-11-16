key = "921242739dac433db87fc7edd6b719ca"
endpoint = "https://nzx.cognitiveservices.azure.com/"

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Authenticate the client using your key and endpoint
def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint,
            credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

# Example method for summarizing text
def sample_extractive_summarization(client):
    from azure.core.credentials import AzureKeyCredential
    from azure.ai.textanalytics import (
        TextAnalyticsClient,
        ExtractSummaryAction
    )

    document = [
        "An Indian-origin top executive of a pharmaceutical company in the US state of New Jersey was shot dead by a gunman who followed him home from a casino for robbery, media reports said on Saturday." 
        "Sree Ranga Aravapalli, 54, a resident of New Jersey's Plainsboro, was killed shortly after arriving home by a gunman who, according to authorities, followed him from a casino outside Philadelphia at around 3:30 AM (local time) on Tuesday, the CBC New York newspaper reported."

'The "wealthy pharmaceutical executive" was followed for 50 miles (80 kms) from a Pennsylvania casino to his New Jersey home where he was murdered in an attempted robbery while his wife and daughter were sleeping, the New York Post newspaper quoted the police as saying.'

"Aravapalli cashed out his night's big winnings, about USD 10,000, in the early morning hours of Tuesday at the Parx Casino in Bensalem when he was spotted with the loot by 27-year-old Jekai Reid-John, of Pennsylvania's Norristown, the Post report said."

"The police have arrested Jekai Reid-John and charged him with first-degree murder."

"Reid-John, who did not know Aravapalli, followed him in his car as he drove back to his quiet, affluent neighbourhood in Plainsboro, according to the Middlesex County Prosecutor's Office."

"Plainsboro Township Police Department Chief Frederick Tavener offered his condolences to Avarapalli's family, who was reportedly well known in the local community."

'"I want to offer my sincerest condolences to the Aravapalli family for their tragic loss. This is an unexpected and alarming event for their family, friends and our entire community," he said in a statement on Wednesday.'

'Aravapalli is survived by his wife, a son and a daughter.'

'Since 2014, Aravapalli was the CEO of Aurex Laboratories, which is described online as a pharmaceutical company that develops clinical supplies, tablets and soft gelatin capsules.'

"In a statement, Parx Casino CEO Eric Hausler condoled Aravapalli's death and said it is cooperating fully with local and state law enforcement agencies in both Pennsylvania and New Jersey and will continue to do so."

'"We are deeply saddened by the report that earlier this week a customer of Parx Casino was the victim of a homicide at his home after returning from a visit to the casino".'

'"We have learned that law enforcement officials have arrested a suspect who followed the victim home from the casino that night. Our sincere condolences go out to the family and friends of the victim at this incredibly difficult time," Hausler said.'

"Neighbours said that Aravapalli and his family called their secluded community home for just a few years."

"It's crazy, I mean, unbelievable. How can somebody follow him all the way and come here and kill him in the night? It's so shocking,\" said neighbour Sheeza Khan."

"It was very shocking for the whole community. It is scary, Khan said."

'"Just a nice family man, always home and there with his wife and kids, and celebrating all the festivals.'

'"What we want to remember about him is that he gave everything. In his 54 years, I think, he probably gave more than most people would in a full 85-year lifespan," said Abhi Kanitkar.'

"Aravapalli's family laid him to rest on Thursday, the report added."
    ]

    poller = client.begin_analyze_actions(
        document,
        actions=[
            ExtractSummaryAction(MaxSentenceCount=4)
        ],
    )

    document_results = poller.result()
    for result in document_results:
        extract_summary_result = result[0]  # first document, first result
        if extract_summary_result.is_error:
            print("...Is an error with code '{}' and message '{}'".format(
                extract_summary_result.code, extract_summary_result.message
            ))
        else:
            print("Summary extracted: \n{}".format(
                " ".join([sentence.text for sentence in extract_summary_result.sentences]))
            )

sample_extractive_summarization(client)