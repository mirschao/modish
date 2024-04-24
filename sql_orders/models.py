from tortoise import fields, Model


class SqlOrders(Model):
    order_id = fields.IntField(pk=True)
    order_sql = fields.TextField()
    order_status = fields.CharField(128)

    def __str__(self):
        return self.order_id
