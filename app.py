from common import db_url, db_meta
from connect import app
from moderation import permission_index

# this shouldn't be done when alembic is accessing the database
if db_url == "sqlite://" or db_url == "sqlite:///app.db":
    db_meta.create_all()

permission_index.initialize()

if __name__ == "__main__":  # test only
    app.run(debug=True)
