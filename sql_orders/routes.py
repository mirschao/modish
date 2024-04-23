from sanic import Blueprint, response
from .controllers import *


sqlorder_urls = Blueprint(name='sqlorders', url_prefix='/sqlorders')

@sqlorder_urls.route(uri='/submit', methods=['POST'])
async def submit_sqlorder_change_route(request):
    data = request.json
    print(data)
    return response.json(data)
