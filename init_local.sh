#mysql create user 'root';
#mysql create datebase 'stepicdb';
#mysql GRANT ALL ON stepicdb* TO 'root';
mysql -uroot -e "CREATE USER root";
mysql -uroot -e "CREATE DATABASE stepicdb";
mysql -uroot -e "GRANT ALL ON stepicdb.* TO 'root'";
