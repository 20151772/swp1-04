from cgi import parse_qs
from template import html

def application(environ, start_response):
	qs = parse_qs(environ['QUERY_STRING'])
	a = qs.get('a', [''])[0]
	b = qs.get('b', [''])[0]

	sum = ""
	multi = ""
	
	try:
		a, b = int(a), int(b)
	
		int_sum = a + b
		int_multi = a * b	

		sum =  str(int_sum)
		multi = str(int_multi)

	except:
		pass	

	response_body = html % {'sum':sum, 'multi':multi}
	start_response('200 OK', [
		('Content-Type', 'text/html'),
		('Content-Length', str(len(response_body)))
	])
	
	return [response_body]
