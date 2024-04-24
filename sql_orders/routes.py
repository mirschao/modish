from sanic import Blueprint, response
from .models import SqlOrders
from .controllers import *


sqlorder_urls = Blueprint(name='sqlorders', url_prefix='/sqlorders')

@sqlorder_urls.route(uri='/submit', methods=['POST'])
async def submit_sqlorder_change_route(request):
    data = request.json
    await SqlOrders.create(
        order_sql = data.get('order_sql'),
        order_status = data.get('order_status')
    )
    return response.json(data)


@sqlorder_urls.route(uri='/query', methods=['GET'])
async def query_sqlorder_detail_route(request):
    data = await SqlOrders.all()
    result = []
    for generator in data:
        items = dict([item for item in generator])
        result.append(items)
    return response.json(result)

