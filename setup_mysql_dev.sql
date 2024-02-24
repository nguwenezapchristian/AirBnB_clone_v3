-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;



72704b6c-a17f-4c9c-b719-d389cee7b569 state
6f6324e9-7057-454d-91a4-291c8c448caa user

af57df5e-49a1-4160-8c66-90c32a995b40 san jose city

place 0778dafd-aa8f-4e54-97db-49111b3f0986

b3032bec-bfb1-49a1-8588-77312985ca60 review
