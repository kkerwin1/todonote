from devToken import token as _token
from evernote import EvernoteClient

client = EvernoteClient(token=_token)
userToken = client.get_user_store()
user = userStore.getUser()
print user.username