import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "29794930"))
    API_HASH = os.environ.get("API_HASH", "2713ab0e7bf2c21f6cc590625920def7")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6349330284:AAGkzAq9Skio25m2VpmKOlUy7urvXMstz4k")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOHIBu4bCGyx6iHI3fjGEBg_DhrUeKoDBZU2z8MYcqyrrUA0BcEHssP-7mAFqLlF4pNZOpMZloRKLuIWyQM0iFElN_lZ93oD3tqZVzzOhDwyAhgmfXnAjNBkQWHdHyWq8NnMiWFhCHFZZDr8vXWKNPwDjLaapna9X44MpJ2MpeO6zFQEpPcRmLwsBrW71kfDJ4ppxkguZ32bjwPySvP659UTFExcrX3YVWxkpXDV50ONCIn55BRH_EcTeS1qIhHrGk1vOgxevedIaLIKOtbA5hTUCP11TAfJB225-X14CzF6PZKLCtSiNi0aY6hoxSLXONEi_ORYkOX9oUDI8zMnyh3xVM3A=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Megha_Chander_MusicBot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/612b4483b2ed270c4070a.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://i.ibb.co/PGFHWDr/MUSIC-BOT.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "6391769382")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
