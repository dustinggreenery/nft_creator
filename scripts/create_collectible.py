from brownie import NFT_Creator
from scripts.helpful_scripts import get_account
from web3 import Web3


def create_collectible():
    account = get_account()
    nft_creator = NFT_Creator[-1]
    creation_tx = nft_creator.createCollectible({"from": account})
    creation_tx.wait(1)
    print("Collectible created!")


def main():
    create_collectible()
