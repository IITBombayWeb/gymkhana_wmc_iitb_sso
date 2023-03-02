# gymkhana_wmc_iitb_sso
# Integrating Django with Apache

Here are the steps to integrate Django with Apache:

1. Copy the `ldap-oauth2` folder to the path `/var/www`.

2. Copy the configuration file (`000-default.conf`) in the `sso_conf_files` folder to `/etc/apache2/sites-enabled/`.

3. Enable HTTPS by running the following commands:

        apt-get update
        apt-get install apache2 openssl
        a2enmod ssl
        a2enmod rewrite
        mkdir /etc/apache2/certs
        cd /etc/apache2/certs
        openssl req -new -newkey rsa:4096 -x509 -sha256 -days 365 -nodes -out apache-certificate.crt -keyout apache.key

