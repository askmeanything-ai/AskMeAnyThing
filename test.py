import requests


SYSTEM_MESSAGE  =  """
You are an personal assistant specifically made for managing the questions being asked to a particualar person.

You have a list of questions.

If questions are related ,You group the related questions. For example 
one person might have asked : what is the color of the sky.
another person might have asked : why is sky blue.
here they are asking about the same subject sky.
so you can combine the questions and make it as : what is the color of the sky ? and why ?

Make the question concise, simple, direct

give the output as numbered questions. don't give what you have done and all. you should return just a list of questions after processing

keep the questions short
NOTE: all the questions are directed to a person not you

"""

question = {
    "model" : "llama3.1:8b",
    "messages" :[
        {
            "role" : "system",
            "content": SYSTEM_MESSAGE
        },
        {
            "role" : "user",
            "content": "what is gpt?, why do you wear same dress?, do you like llm? , what is llm"
        }
    ],
    "stream": False

}

response = requests.post("http://localhost:11434/api/chat",json=question)

print(response.text)

