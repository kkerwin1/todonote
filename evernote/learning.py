from devToken import token as _token
from evernote.api.client import EvernoteClient

client = EvernoteClient(token=_token)
userToken = client.get_user_store()
user = userStore.getUser()
print user.username