from time import sleep
import configparser

config = configparser.ConfigParser()
config.read('config.ini')


# Common functions here

def generateCert(domain):
    print("Generating certificate for: "+domain)
    cert = "foo-"+domain

    sleep_time = int(config['system']['sleep_time'])
    
    print("Sleeping for " + str(sleep_time) + "s...")
    sleep(sleep_time)
    return cert