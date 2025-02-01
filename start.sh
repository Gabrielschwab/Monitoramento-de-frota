#!/bin/bash
waitress-serve --listen=0.0.0.0:10000 Monitoramento-de-frota.wsgi:application
