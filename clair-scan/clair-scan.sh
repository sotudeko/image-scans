#!/bin/bash

rm -rf ./output
mkdir output

#docker run -d --name clair-db arminc/clair-db:latest
#docker run -p 6060:6060 -p 6061:6061 --link clair-db:postgres -d --name clair arminc/clair-local-scan:v2.0.8_0ed98e9ead65a51ba53f7cc53fa5e80c92169207

#https://github.com/arminc/clair-scanner/releases
myhostname=miles.local
./clair-scanner_darwin_amd64 --ip ${myhostname} -r output/clair-scanner-output.json centos:latest

java -jar /opt/nxiq/nexus-iq-cli -i centos-clair -s http://localhost:8070 -a admin:admin123 output

