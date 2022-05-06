from celery import shared_task
from crypto.models.Asset import Asset

asset = Asset()


@shared_task
def update_bitcoin_price_usd():
    asset.update_asset_price('BTC', 'USD')


@shared_task
def update_bitcoin_price_pln():
    asset.update_asset_price('BTC', 'PLN')


@shared_task
def update_bitcoin_price_eur():
    asset.update_asset_price('BTC', 'EUR')


@shared_task
def update_bitcoin_price_on_server():
    asset.update_asset_in_server('BTC')


@shared_task
def update_eth_price_usd():
    asset.update_asset_price('ETH', 'USD')


@shared_task
def update_eth_price_pln():
    asset.update_asset_price('ETH', 'PLN')


@shared_task
def update_eth_price_eur():
    asset.update_asset_price('ETH', 'EUR')


@shared_task
def update_eth_price_on_server():
    asset.update_asset_in_server('ETH')

