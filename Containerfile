FROM registry.access.redhat.com/ubi8/nginx-118

MAINTAINER Gregory Bennett <gregory@digital.mod.uk>

# Add application sources
ADD site/*.html .

# Run script uses standard ways to run the application
CMD nginx -g "daemon off;"
