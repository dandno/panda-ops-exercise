#!/usr/bin/python
import sys
import argparse
from urllib2 import Request, urlopen, URLError
import subprocess
import requests
import tarfile

# -------------------------------------------------------------------
# --           M A I N   S E C T I O N         										 --
# --  				 --
# --  		                     												       --
# -------------------------------------------------------------------


def _health_check(url):
        req = Request(url)
        try:
           response = urlopen(req)
           answer = response.read()
           print "Health check status is " + answer
        except URLError as e:
            if hasattr(e, 'reason'):
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
            elif hasattr(e, 'code'):
                 print 'The server couldn\'t fulfill the request.'
                 print 'Error code: ', e.code
        else:
            print "Health check is OK"


def _run_compose(operation):
        command=["docker-compose", operation]
        try:
            compse=subprocess.call(command)
        except Exception as e:
            print(e)


def _download_and_extract(url, destination):
        command=["wget", "-c", "-P", destination, url]
        try:
            download_state=subprocess.call(command)
        except Exception as e:
            print(e)
        #if download_state==0 => successfull download
        if download_state == 0:
           tar_name = url.split('/')
           tar_name = tar_name[-1]
           fname = destination + "/" + tar_name
           tar = tarfile.open(fname, "r:gz")
           tar.extractall(path=destination)
           tar.close()          

def main(argv):
	parser = argparse.ArgumentParser(description="Running flow for panda")
	parser.add_argument('-images_url',action="store",dest="images_url",help="Images tar url",required=True)
	parser.add_argument('-images_dir',action="store",dest="images_dir",help="Images directory",required=True)
	parser.add_argument('-health_check_url',action="store",dest="health_check_url",help="Container url",required=True)
	
	bigpanda = parser.parse_args()
  _download_and_extract(bigpanda.images_url,bigpanda.images_dir)
  _run_compose('up')
	_health_check(bigpanda.health_check_url)	
	
if __name__ == "__main__":
    main(sys.argv)

