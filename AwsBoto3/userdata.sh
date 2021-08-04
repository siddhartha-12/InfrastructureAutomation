#!/bin/bash
sudo apt-get -y update
sudo apt-get -y install apache2
sudo apt-get -y install git
systemctl start apache2
systemctl enable apache2
git clone https://github.com/siddhartha-12/InfrastructureAutomation.git
mv InfrastructureAutomation/AwsBoto3/index.html /var/www/html/index.html
systemctl reload apache2
systemctl restart apache2
