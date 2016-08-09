def application(env, start_response):
#    status = "200 OK"
#    response_headers = [('Content-Type','
    start_response('200 OK', [('Content-Type', 'text/plain')])
    resp = env['QUERY_STRING'].split("&")
    resp = [item+"\r\n" for item in resp]  
    return resp
