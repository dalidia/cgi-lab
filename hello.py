#!/usr/bin/env python3
import os

print("Content-Type: text/html")
print()
print(f"<p>QUERY_STRING={os.environ['QUERY_STRING']}<p>")
print(f"<p>USER_BROWSER={os.environ['HTTP_USER_AGENT']}<p>")
