from common import db_url, db_meta
from connect import app
from moderation import permission_index

# this shouldn't be done when alembic is accessing the database
permission_index.initialize()

if db_url == "sqlite://":
    db_meta.create_all()

if __name__ == "__main__":  # test only
    app.run(debug=True)
