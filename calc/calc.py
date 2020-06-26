from cgi import parse_qs
from template import html

def application(environ, start_response):
	qs = parse_qs(environ['QUERY_STRING'])
	a = qs.get('a', [''])[0]
	b = qs.get('b', [''])[0]

	sum = ""
	multi = ""
	err_msg = ""
	
	try:
		a, b = int(a), int(b)
	
		int_sum = a + b
		int_multi = a * b	

		sum =  str(int_sum)
		multi = str(int_multi)

	except:
		try:
			if a is '':  # a='',b='int'
				b = int(b)
				err_msg = "Empty Value"
				
			elif b is '':  # b='',a='int' 
				a = int(a)
				err_msg = "Empty Value"

			else:  # a='int',b='str' or b='str',a='int'
				err_msg = "Wrong Type of Value"	

		except:
			if a is '' and b is '':  # a='',b='' 
				err_msg = ""

			else:  # a='',b='str' or a='str',b='' or a='str',b='str' 
				err_msg = "Wrong Type of Value"
	
	response_body = html % {'sum':sum, 'multi':multi, 'err_msg':err_msg}
	start_response('200 OK', [
		('Content-Type', 'text/html'),
		('Content-Length', str(len(response_body)))
	])
	
	return [response_body]
