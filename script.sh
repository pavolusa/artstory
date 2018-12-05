#!/bin/bash

docker-compose run web django-admin.py startproject code_artstory .
docker-compose run web django-admin.py startapp artstory

cd artstory/
rm -rf admin.py models.py views.py
cd - 

cp ./src/artstory/admin.py ./artstory/
cp ./src/artstory/models.py ./artstory/
cp ./src/artstory/views.py ./artstory/
cp -r ./src/artstory/templates/ ./artstory/
 
cd code_artstory
rm -rf urls.py

num_line_setting=$(grep -n -w "INSTALLED_APPS" settings.py | awk -F ':' '{print $1}')
num_line_setting=$((num_line_setting+1))

str_line_setting="'artstory.apps.ArtstoryConfig',"
ex -s -c $num_line_setting'i|'$str_line_setting -c x settings.py

num_line_setting=$(grep -n -w "SECRET_KEY" settings.py | awk -F ':' '{print $1}')
str_line_setting='ADMIN_SITE_HEADER="ArtStory.vn"'
ex -s -c $num_line_setting'i|'$str_line_setting -c x settings.py

cd -
cp -r ./src/code_artstory/urls.py ./code_artstory/

cat ./code_artstory/settings.py media.txt >> tmp.py
mv tmp.py ./code_artstory/settings.py

cat ./code_artstory/settings.py staticfiles_dirs.txt >> tmp.py
mv tmp.py ./code_artstory/settings.py

docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser
