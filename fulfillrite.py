from pyactiveresource import activeresource as ar

_SITE = 'https://my.fulfillrite.com/api/products'


class FulfillriteResource(ar.ActiveResource):
    """
    ActiveResource for interacting with Fulfillrite API.
    """
    _site = _SITE


class Orders(FulfillriteResource):
    """
    ActiveResource for Fulfillrite Orders API endpoint.
    """
    pass


class Products(FulfillriteResource):
    """
    ActiveResource for Fulfillrite Products API endpoint.
    """
    pass
