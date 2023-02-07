from chatterbot import ChatBot

from chatterbot.trainers import ChatterBotCorpusTrainer

from twilio.rest import Client

# Initialize the ChatBot model

bot = ChatBot('Customer Service Bot')

# Train the ChatBot model with customer service questions and answers

trainer = ChatterBotCorpusTrainer(bot)

trainer.train('chatterbot.corpus.english.greetings',

              'chatterbot.corpus.english.conversations')

# Twilio credentials

account_sid = 'YOUR_TWILIO_ACCOUNT_SID'

auth_token = 'YOUR_TWILIO_AUTH_TOKEN'

client = Client(account_sid, auth_token)

# Receive incoming messages from WhatsApp

def receive_message():

    messages = client.messages.list(to='whatsapp:+14155238886')

    for message in messages:

        return message.body

# Respond to incoming messages from WhatsApp

def respond_to_message(message):

    response = bot.get_response(message)

    client.messages.create(to='whatsapp:+14155238886',

                           from_='whatsapp:+14155238886',

                           body=response)

# Main function to run the chatbot

def main():

    message = receive_message()

    respond_to_message(message)

# Run the chatbot

if __name__ == '__main__':

    main()

