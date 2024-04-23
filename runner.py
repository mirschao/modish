from sanic import Sanic
from config import default
from sql_orders.routes import sqlorder_urls


def create_app(config_object=default):
    app = Sanic(__name__)

    # update configure.
    app.update_config(config_object.TestingConfig)

    # registry blueprint.
    app.blueprint(sqlorder_urls)

    return app


app = create_app()


if __name__ == '__main__':
    app.run(
        host='0.0.0.0', port=3364
    )

