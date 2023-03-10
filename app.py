import sys
import logging
from slack_bolt import App
from slack_sdk.web import WebClient
from slack_service import SlackService

# Initialize a Bolt for Python app
for i in range(len(sys.argv)):
    print(sys.argv[i])

token = ''
channel_id = ''
channel_name = ''

if len(sys.argv) > 2:
    token = sys.argv[1] #'xoxb-4720168470421-4736004577841-15xH9rDsk8Ylh0sTxlnLMyqz'
    channel_id = sys.argv[2] #'C04LUGX0CT1'
    channel_name = sys.argv[3] #'a-project'
else:
    print('Please pass required arguments!')
    exit(1)

print(token, channel_id, channel_name)

app = App(token=token)
#conversation_id = 'C04LUGX0CT1'

# WebClient instantiates a client that can call API methods
# When using Bolt, you can use either `app.client` or the `client` passed to listeners.
def sendMessage(client):
    logger = logging.getLogger(__name__)
    try:
        if channel_name is not None:
            result = client.chat_postMessage(
                channel= channel_id,
                text= "Hi Team, Good Morning!!"
            )
            #Print result
            print(f"Message status: {result}")

    except SlackApiError as e:# noqa
        print(f"Error: {e}")
    
def updateMessage(client):
    logger = logging.getLogger(__name__)
    try:
        if channel_name is not None:
            result = client.chat_update(
                channel= channel_id,
                text= "Hi Team, This is updated message from python script!!",
                ts="1675165232.425259"
            )
            #Print result
            print(f"Message status: {result}")

    except SlackApiError as e:# noqa
        print(f"Error: {e}")

def getMessage(client):
    logger = logging.getLogger(__name__)
    try:
        # Call the conversations.list method using the WebClient
        if channel_id is not None:
            result = client.conversations_history(
                channel=channel_id,
                #inclusive=True,
                #oldest="1610144875.000600",
                limit=10
            )
            #Print result
            print(f"Found conversation ID: {channel_id}: \n Message: {result}")

    except SlackApiError as e:# noqa
        print(f"Error: {e}")

if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    sendMessage(app.client)
    #getMessage(app.client)
    #updateMessage(app.client)
    #app.start(3000)
