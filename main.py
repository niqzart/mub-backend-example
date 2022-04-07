from datetime import timedelta

from common import app, db_meta, db_url  # noqa

jwt = app.configure_jwt_with_loaders(["cookies"], timedelta(hours=72), print)
api = app.configure_restx()

# add your namespaces here via `api.add_namespace(<namespace>)`

if __name__ == "__main__":  # test only
    app.run(debug=True)
