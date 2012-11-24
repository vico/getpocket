#Python module for adding url to getpocket (API v3)

getpocket [api v3](http://getpocket.com/developer/docs/overview)

### getpocket.get_request_token(consumer_key,url,redirect_uri)

take [consumer_key](http://getpocket.com/developer/apps/new ), a url to add, a redirect url
and return a dictionary that contains 'request_token' if success,
or return a dictionary that contains error messages with keys are 'http-status','x-error-code','x-error'

### get_access_token(consumer_key,code)

take consumer_key, a request_token returned by get_request_token
and return a dictionary that contains 'access_code' if success,
or return a dictionary that contains error messages with keys are 'http-status','x-error-code','x-error'

### add(consumer_key,access_token,url)

take consumer_key, a access_token returned by get_access_token, a url to add
and return a dictionary that contains 'status' if success (status == 1),
or return a dictionary that contains error messages with keys are 'http-status','x-error-code','x-error'

