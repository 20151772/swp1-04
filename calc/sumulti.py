from cgi import parse_qs
from template2 import html
from PIL import Image, ImageDraw, ImageFont

def application(environ, start_response):
	qs = parse_qs(environ['QUERY_STRING'])
	a = qs.get('a', [''])[0]
	b = qs.get('b', [''])[0]

	font_addr = '/usr/share/fonts/truetype/freefont/FreeSans.ttf'
	fnt = ImageFont.truetype(font_addr,50)

	img1 = Image.new('RGB', (500,50), (255,255,255))
	img2 = Image.new('RGB', (500,50), (255,255,255))
	
	if '' not in [a, b]:
		a, b = int(a), int(b)

		sum = a + b
		multi = a * b

		draw_sum = ImageDraw.Draw(img1)
		draw_multi = ImageDraw.Draw(img2)
		draw_sum.text((50,0),str(sum),fill='black',font=fnt)
		draw_multi.text((50,0),str(multi),fill='black',font=fnt)	

	img1.save('/var/www/html/img/sum.png')
	img2.save('/var/www/html/img/multi.png')

	response_body = html
	start_response('200 OK', [
		('Content-Type', 'text/html'),
		('Content-Length', str(len(response_body)))
	])
	
	return [response_body]
