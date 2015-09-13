from devToken import token as _token	

client = EvernoteClient(token=_token)
userToken = client.get_user_store()
user = userStore.getUser()
print user.username