FROM php:7.3-apache

#Shared layer between rainloop and roundcube
RUN apt-get update && apt-get install -y \
  python3 curl python3-pip git python3-multidict \
  && rm -rf /var/lib/apt/lists \
  && echo "ServerSignature Off" >> /etc/apache2/apache2.conf

# Shared layer between nginx, dovecot, postfix, postgresql, rspamd, unbound, rainloop, roundcube
RUN pip3 install socrate

ENV RAINLOOP_URL https://github.com/RainLoop/rainloop-webmail/releases/download/v1.13.0/rainloop-community-1.13.0.zip

RUN apt-get update && apt-get install -y \
      unzip python3-jinja2 \
 && rm -rf /var/www/html/ \
 && mkdir /var/www/html \
 && cd /var/www/html \
 && curl -L -O ${RAINLOOP_URL} \
 && unzip -q *.zip \
 && rm -f *.zip \
 && rm -rf data/ \
 && find . -type d -exec chmod 755 {} \; \
 && find . -type f -exec chmod 644 {} \; \
 && chown -R www-data: * \
 && apt-get purge -y unzip \
 && rm -rf /var/lib/apt/lists \
 && sed -i "s/80/5000/g" /etc/apache2/sites-available/000-default.conf /etc/apache2/ports.conf

COPY include.php /var/www/html/include.php
COPY php.ini /php.ini

COPY application.ini /application.ini
COPY default.ini /default.ini

COPY start.py /start.py

EXPOSE 5000/tcp
VOLUME ["/data"]

CMD /start.py

HEALTHCHECK CMD curl -f -L http://localhost/ || exit 1
