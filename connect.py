from datetime import timedelta

from common import app
from common import db_meta, db_url  # noqa  # for alembic
from moderation import mub_cli_blueprint, superuser_namespace, mub_base_namespace

app.register_blueprint(mub_cli_blueprint)
jwt = app.configure_jwt_with_loaders(["cookies"], timedelta(hours=72), print)
api = app.configure_restx()

api.add_namespace(mub_base_namespace)
api.add_namespace(superuser_namespace)
# add your namespaces here via `api.add_namespace(<namespace>)`
