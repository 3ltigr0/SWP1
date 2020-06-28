from cgi import parse_qs
from templatesm import html

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    a = d.get('a', [''])[0]
    b = d.get('b', [''])[0]
    s = ''
    t = ''
    x = ''
    y = ''
    if '' not in [a, b]:
        a = int(a)
        b = int(b)
        x = str(a+b)
        y = str(a*b)
    else:
        s = 'Please enter value'
    response_body = html % (s, x, y) #+ 'sum: ' + str(x) + ' mul: ' + str(y)
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ])
    return [response_body]
