# pylint: disable=E1101

from src.infra.config import DBConnectionHandler
from src.infra.entities import Users


class Fakerepo:
    """A simple repository"""

    @classmethod
    def inser_use(cls):
        """something"""

        with DBConnectionHandler() as db_connection:
            try:
                new_user = Users(name="Programador", password="123")
                db_connection.session.add(new_user)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
