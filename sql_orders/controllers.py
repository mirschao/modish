from .models import SqlOrders


async def sqlorder_create(request_data):
    data = ''
    await SqlOrders.create(data)
    return 
