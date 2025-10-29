FROM mysql:8.0

# Copy the SQL schema file
COPY lms.sql /docker-entrypoint-initdb.d/

# Environment variables
ENV MYSQL_ROOT_PASSWORD=rootpassword
ENV MYSQL_DATABASE=lms
ENV MYSQL_USER=lmsuser
ENV MYSQL_PASSWORD=lms123