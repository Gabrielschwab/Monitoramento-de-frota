#!/bin/bash
waitress-serve --listen=0.0.0.0:10000 myproject.wsgi:application
