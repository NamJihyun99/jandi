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
# Expires September 8, 1995                                  March 8, 1995
#
# URL: http://www.ics.uci.edu/pub/ietf/http/draft-ietf-http-v10-spec-00.txt
#
# and
#
# Network Working Group                                      R. Fielding
# Request for Comments: 2616                                       et al
# Obsoletes: 2068                                              June 1999
# Category: Standards Track
#
# URL: http://www.faqs.org/rfcs/rfc2616.html

# Log files
# ---------
#
# Here's a quote from the NCSA httpd docs about log file format.
#
# | The logfile format is as follows. Each line consists of:
# |
# | host rfc931 authuser [DD/Mon/YYYY:hh:mm:ss] "request" ddd bbbb
# |
# |        host: Either the DNS name or the IP number of the remote client
# |        rfc931: Any information returned by identd for this person,
# |                - otherwise.
# |        authuser: If user sent a userid for authentication, the user name,
# |                  - otherwise.
# |        DD: Day
# |        Mon: Month (calendar name)
# |        YYYY: Year
# |        hh: hour (24-hour format, the machine's timezone)
# |        mm: minutes
# |        ss: seconds
# |        request: The first line of the HTTP request as sent by the client.
# |        ddd: the status code returned by the server, - if not available.
# |        bbbb: the total number of bytes sent,
# |              *not including the HTTP/1.0 header*, - if not available
# |
# | You can determine the name of the file accessed through request.
#
# (Actually, the latter is only true if you know the server configuration
# at the time the request was made!)

__version__ = "0.6"

__all__ = [
    "HTTPServer", "ThreadingHTTPServer",
    "HTTPSServer", "ThreadingHTTPSServer",
    "BaseHTTPRequestHandler", "SimpleHTTPRequestHandler",
]

import datetime
import email.utils
import html
import http.client
import io
import itertools
