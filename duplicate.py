import openai

class Chatbot:
    def _init_(self):
        openai.api_key = "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"
    def get_response (self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5
        ). choices[0].text
        return response

if __name__ =="__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a joke about birds.")
    print(response)