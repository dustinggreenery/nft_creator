from scripts.helpful_scripts import get_account
from brownie import NFT_Creator


def deploy():
    account = get_account()
    nft_creator = NFT_Creator.deploy({"from": account})
    return nft_creator


def main():
    deploy()
