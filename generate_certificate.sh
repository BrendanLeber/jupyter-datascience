#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# SSL
# Generate cert like this:

openssl req -x509 -nodes -newkey rsa:2048 -keyout jupyter.pem -out jupyter.pem
