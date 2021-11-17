# uuid-service

To set up the environment, run the following from the root folder of the service:

    python3 -m venv env
    source env/bin/activate
    mkdir data
    sqlite3 -init create-db.sql data/uuid-db.db ""
    pip3 install -r requirements.txt
  
Run the server with:

    python3 -m swagger-server

Create new UUIDs with: 

    curl -i -X POST http://localhost:8080/uuid
  
Check UUIDs with:

    curl -i -X GET http://localhost:8080/uuid/{uuid}
  
where {uuid} is a valid UUID (e.g. d4114db6-4d9b-4129-b7d9-858b5e6d4b6b)
