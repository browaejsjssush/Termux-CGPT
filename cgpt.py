print ("CHATGPT Bot")
print ("Credits: Pydroid3 pip, Codingthe smartway.com")
print ("WARNING: bot may spew nonsense")
print ("WARNING: this version of the chatbot is very old, this means its very untrustworthy")
print (".")
print ("Enter your text:")
	
import openai

openai.api_key = "put api herr"



model_engine = "text-davinci-003"
prompt = input("")


completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print(response)
