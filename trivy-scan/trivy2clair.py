import sys
import os
import json

trivyFile = "./trivy-report.json"
clairFile = "./output/clair-scanner-output.json"

def readTrivyFile():
  clairJson = {}
  vulnerabilities = []

  with open(trivyFile) as trivyJsonfile:
    data = json.load(trivyJsonfile)
    d = data[0]

    imageName = d["Target"]
    clairJson['image'] = imageName

    for t in d["Vulnerabilities"]:
      vulnerability = ""
      pkg = ""
      version = ""
      severity = ""
      link = ""
      fixedBy = ""
      namespace = ""
      description = ""
       
      
      severity = t['Severity']
      link = t['PrimaryURL']
	
      if "VulnerabilityID" in t.keys():
        vulnerability = t['VulnerabilityID']
      
      if "PkgName" in t.keys():
        pkg = t['PkgName']

      if "InstalledVersion" in t.keys():
        version = t['InstalledVersion']

      if "Severity" in t.keys():
        severity = t['Severity']

      if "PrimaryURL" in t.keys():
        link = t['PrimaryURL']

      if "FixedVersion" in t.keys():
        fixedBy = t['FixedVersion']

      if "SeveritySource" in t.keys():
        namespace = t['SeveritySource']

      if "Description" in t.keys():
        description = t['Description']
 
      v = {'vulnerability': vulnerability, 
           'featurename': pkg, 
           'featureversion': version, 
           'severity': severity.title(), 
           'link': link, 
           'fixedBy': fixedBy,
           'namespace': "centos-8",
           'description': description
           }

      vulnerabilities.append(v)
    
    clairJson['vulnerabilities'] = vulnerabilities

  return clairJson

def writeClairJson(jsonData):

  if os.path.exists(clairFile):
    os.remove(clairFile)

  with open(clairFile, 'w') as fd:
    json.dump(jsonData, fd, indent=4)
  
  


def main():
  data = readTrivyFile()
  writeClairJson(data)



if __name__ == '__main__':
  main()
