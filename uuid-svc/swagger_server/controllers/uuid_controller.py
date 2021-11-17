import connexion
import six
import sqlite3
import uuid

from swagger_server.models.uuid import Uuid  # noqa: E501
from swagger_server import util

db_file="data/uuid-db.db"

def generate_uuid():  # noqa: E501
    """Request the generation and allocation of a UUID

     # noqa: E501


    :rtype: Uuid
    """
    db = sqlite3.connect(db_file)
    cursor = db.cursor()
    while True:
        myuuid = uuid.uuid4()
        sql = "SELECT count(1) FROM uuids WHERE uuid = ?"
        args = (str(myuuid),)
        cursor.execute(sql,args)
        if not cursor.fetchone()[0]:
            break

    sql = "INSERT INTO uuids VALUES (?)"
    args = (str(myuuid),)
    try:
        cursor.execute(sql,args)
        db.commit()
    except sqlite3.Error as error:
        print (error)
        return "Internal server error", 500

    db.close()
    return myuuid


def get_uuid(uuidstr):  # noqa: E501
    """Determine if a provided UUID has been allocated and is valid

    For valid response try UUIDs of the form \&quot;3fa85f64-5717-4562-b3fc-2c963f66afa6\&quot;. Other values will generated exceptions # noqa: E501

    :param uuidstr: uuid that needs to be validated
    :type uuidstr: 

    :rtype: None
    """

    try:
        val = uuid.UUID(uuidstr)
    except ValueError:
        return "Bad Request", 400

    db = sqlite3.connect(db_file)
    cursor = db.cursor()

    sql = "SELECT count(1) FROM uuids WHERE uuid = ?"
    args = (str(val),)
    cursor.execute (sql,args)
    if cursor.fetchone()[0]:
        rv = 200
    else:
        rv = 404
    db.close()
    
    return val, rv

