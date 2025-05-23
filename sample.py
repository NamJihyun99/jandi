print('Hello World!')
"""HTTP server classes.

Note: BaseHTTPRequestHandler doesn't implement any HTTP request; see
SimpleHTTPRequestHandler for simple implementations of GET, HEAD and POST.

It does, however, optionally implement HTTP/1.1 persistent connections.

XXX To do:

- log requests even later (to capture byte count)
- log user-agent header and other interesting goodies
- send error log to separate file
"""


# See also:
#
# HTTP Working Group                                        T. Berners-Lee
# INTERNET-DRAFT                                            R. T. Fielding
# <draft-ietf-http-v10-spec-00.txt>                     H. Frystyk Nielsen
