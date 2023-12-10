# Use Ubuntu 20.04 as the base image
FROM ubuntu:20.04

# Set the timezone to Europe/Brussels
ENV TZ=Europe/Brussels
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Update the package list and install lighttpd
RUN apt-get update && apt-get install -y lighttpd

# Create the directory for the web content
RUN mkdir -p /var/www/localhost/htdocs

# Copy the index.html file to the web directory
COPY ./index.html /var/www/html/index.html

# Expose port 80 for HTTP traffic
EXPOSE 80

# Start the lighttpd server with the specified configuration file
CMD ["lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]
