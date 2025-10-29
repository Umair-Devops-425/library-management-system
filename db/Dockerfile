FROM mysql:8.0

# Copy the SQL dump file to docker-entrypoint-initdb.d
COPY lms.sql /docker-entrypoint-initdb.d/

# Set environment variables
ENV MYSQL_ROOT_PASSWORD=rootpassword
ENV MYSQL_DATABASE=lms
ENV MYSQL_USER=lmsuser
ENV MYSQL_PASSWORD=lms123