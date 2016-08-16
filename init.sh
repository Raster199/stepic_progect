#sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
#sudo rm -rf /etc/nginx/sites-enabled/default
#sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
#sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test-gunicorn
sudo ln -sf /home/box/web/etc/django.conf   /etc/gunicorn.d/test-django
#gunicorn -b 0.0.0.0:8080 hello
sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/mysql start
