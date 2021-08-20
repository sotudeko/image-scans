#!/bin/bash

#brew install trivy

rm -rf output
mkdir output

trivy image -f json -o trivy-report.json centos:latest
python3 trivy2clair.py

java -jar /opt/nxiq/nexus-iq-cli -i centos-trivy -s http://localhost:8070 -a admin:admin123 output

