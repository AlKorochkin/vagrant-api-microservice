from vagrant import Vagrant
import os
import requests
import logging

logger = logging.getLogger(__name__)
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger.addHandler(f_format)

def vagrant_up(response_url):
    vg = Vagrant()
    vg.up()
    logger.info("Up done")


def vagrant_destroy(response_url):
    vg = Vagrant()
    vg.destroy()
    logger.info("Destroy done")

if __name__ == "__main__":
    path = "Vagrantfile"
    logger.info("Test vagrant up")
    vagrant_up(path)
    logger.info("Up Done")
    logger.info("Test vagrant Destroy")
    vagrant_destroy(path)
    logger.info("Destroy Done")