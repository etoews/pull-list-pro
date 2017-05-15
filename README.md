# Pull List Pro

```bash
python3 -m venv pulp
source environments/development.env

pip install -r requirements.txt

docker volume create pulp-db
docker run --detach --name pulp-db \
  --env POSTGRES_PASSWORD=${PGPASSWORD} \
  --volume pulp-db:/var/lib/postgresql/data \
  --publish 5432:5432 \
  postgres:9-alpine

createdb --host localhost --username postgres pulp-db-dev
createdb --host localhost --username postgres pulp-db-test

# python manage.py db migrate  # to be run after making a database change
python manage.py db upgrade

psql --host localhost --username postgres pulp-db-dev
# \d
# \d pulllists
# select * from pulllists;
# \q

python test_pulllists.py

docker rm -f pulp-db
docker volume rm pulp-db
```