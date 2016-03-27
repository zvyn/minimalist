#!/usr/bin/bash
ncat -l 8000 -k --sh-exec\
    'echo -e "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nHello World\r\n"'
