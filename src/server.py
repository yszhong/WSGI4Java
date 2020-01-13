from wsgiref.simple_server import make_server
import threading
import simple_work
import socket


def application(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/html")])
    path_info = environ["PATH_INFO"]
    query_string = environ["QUERY_STRING"]
    query_string = query_string.split("&")
    if len(query_string) != 2:
        # raise error
        body = "<h1>" + path_info + query_string + "</h1>"
    else:
        command = " ".join(["python", path_info, query_string[0], query_string[1]])
        body = "<h1>Running \"" + command + "\"...</h1>"
        # run python program with two parameters
        target_function = simple_work.main
        run_thread = threading.Thread(target=target_function, args=query_string)
        run_thread.start()
    body = [body.encode('utf-8')]
    return body


def get_local_host():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip


# http://192.168.0.34:8000/single_test.py?/data3/data/HD/2/&/data3/data/
if __name__ == '__main__':
    # create server:
    ip = get_local_host()
    port = 8000
    httpd = make_server(ip, port, application)
    print("Serving HTTP on " + ip + " with port " + str(port) + "...")
    # start listening HTTP request:
    httpd.serve_forever()
