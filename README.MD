# BackendDesarrollo1

## run project 
```
docker-compose up -d --build
```
## stop project 
```
docker-compose down
```
## run commands on docker image
```
docker-compose exec web python ./your/script
```
for example:
```
docker-compose exec web python manage.py migrate
```
