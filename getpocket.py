import urllib2
import json
import logging

# get the request token (code)
# return request token 
# error: return a list [ HTTP status, x-error-code, x-error]
def get_request_token(consumer_key,url,redirect_uri):
		
	req = urllib2.Request(url='https://getpocket.com/v3/oauth/request',
		data=json.dumps({'consumer_key': consumer_key, 'redirect_uri':redirect_uri}))
	req.add_header('Content-Type','application/json; charset=UTF-8')
	req.add_header('X-Accept','application/json')

	ret = {}

	try:
		f = urllib2.urlopen(req)
		res = json.loads(f.read())
		ret['code'] = res['code']
	except urllib2.HTTPError,e:
		ret['http-status'] = e.code
		ret['x-error-code'] = e.headers['x-error-code']
		ret['x-error'] = e.headers['x-error']
	
	return ret


	

def get_access_token(consumer_key,code):

	req = urllib2.Request(url='https://getpocket.com/v3/oauth/authorize',
		data=json.dumps({'consumer_key': consumer_key, 'code':code}))
	req.add_header('Content-Type','application/json; charset=UTF-8')
	req.add_header('X-Accept','application/json')
	
	ret = {}

	try:
		f = urllib2.urlopen(req)
		res = json.loads(f.read())
		ret['access_token'] = res['access_token']
		ret['username'] = res['username']

	except urllib2.HTTPError,e:
		ret['http-status'] = e.code
		ret['x-error-code'] = e.headers['x-error-code']
		ret['x-error'] = e.headers['x-error']
	
	return ret

def add(consumer_key,access_token,url):
	req = urllib2.Request(url='https://getpocket.com/v3/add',
		data=json.dumps({'url':url,'consumer_key': consumer_key, 'access_token':access_token}))
	req.add_header('Content-Type','application/json; charset=UTF-8')
	req.add_header('X-Accept','application/json')

	ret = {}

	try:
		f = urllib2.urlopen(req)
		res = json.loads(f.read())
		ret['status'] = res['status']
		headers = f.info()
		ret['x-limit-key-remaining'] = headers['x-limit-key-remaining']
		ret['x-limit-key-limit'] = headers['x-limit-key-limit']
		ret['x-limit-user-limit'] = headers['x-limit-user-limit']
		ret['x-limit-key-reset'] = headers['x-limit-key-reset']
		ret['x-limit-user-reset'] = headers['x-limit-user-reset']
		ret['x-limit-user-remaining'] = headers['x-limit-user-remaining']

	except urllib2.HTTPError,e:
		ret['http-status'] = e.code
		ret['x-error-code'] = e.headers['x-error-code']
		ret['x-error'] = e.headers['x-error']

	return ret