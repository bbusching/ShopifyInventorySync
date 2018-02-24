import fulfillrite
import json
import os
import shopify

_SITE = "https://filmwerks.myshopify.com/admin"


def _init_shopify():
    """
    Initialize connection to Shopify.
    """
    shopify.ShopifyResource.site = _SITE
    shopify.ShopifyResource.user = os.environ['SHOPIFY_API_KEY']
    shopify.ShopifyResource.password = os.environ['SHOPIFY_PASSWORD']


def _obtain_skus():
    """"
    Return SKUs for manually tracked products.
    """
    skus = []
    for product in shopify.Product.find():
        for variant in product.variants:
            variant_dict = json.loads(
                variant.to_json().decode('ascii'))['variant']
            if variant_dict['inventory_management'] == 'shopify':
                skus.append(variant_dict['sku'])
    return skus


def main():
    """
    Obtain inventory information from Fulfillrite and update Shopify.
    """
    pass


if __name__ == "__main__":
    main()
