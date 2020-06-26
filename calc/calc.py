from cgi import parse_qs
from template import html

def application(environ, start_response):
	qs = parse_qs(environ['QUERY_STRING'])
	a = qs.get('a', [''])[0]
	b = qs.get('b', [''])[0]

	sum = 0
	multi = 0

	if '' not in [a, b]:
		a, b = int(a), int(b)

		sum = a + b
		multi = a * b
		
	response_body = html % {'sum':sum, 'multi':multi}
	start_response('200 OK', [
		('Content-Type', 'text/html'),
		('Content-Length', str(len(response_body)))
	])
	
	return [response_body]
