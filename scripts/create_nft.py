from turtle import update
from scripts.deploy_and_create import deploy
from scripts.create_collectible import create_collectible
from scripts.create_metadata import create_metadata
from scripts.set_tokenuri import set_token_uri
from customize_nfts import amount_of_nfts


def create_nft():
    deploy()
    for i in range(amount_of_nfts):
        create_collectible()
    ipfs_metadata = create_metadata()
    set_token_uri(ipfs_metadata)


def main():
    create_nft()
