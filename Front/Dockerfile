FROM ubuntu:20.04
ENV TZ=Europe/Brussels
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update && apt-get install -y lighttpd
RUN mkdir -p /var/www/localhost/htdocs
COPY ./index.html /var/www/html/index.html
EXPOSE 80
CMD ["lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]
