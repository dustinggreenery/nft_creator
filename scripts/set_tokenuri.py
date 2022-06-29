from brownie import network, NFT_Creator
from scripts.helpful_scripts import OPENSEA_URL, get_account
from scripts.create_metadata import nft_name


def set_tokenURI(token_id, nft_contract, tokenURI):
    account = get_account()
    tx = nft_contract.setTokenURI(token_id, tokenURI, {"from": account})
    tx.wait(1)
    print(
        f"You can now view NFT at {OPENSEA_URL.format(nft_contract.address, token_id)}"
    )
    print("May take up to 20 minutes, make sure to hit the refresh metadata button")


def set_token_uri(ipfs_metadata):
    print(f"Working on {network.show_active()}")
    nft_creator = NFT_Creator[-1]
    number_of_collectibles = nft_creator.tokenCounter()
    print(f"You have {number_of_collectibles} tokenIds")
    for token_id in range(number_of_collectibles):
        if not nft_creator.tokenURI(token_id).startswith("https://"):
            print(f"Setting tokenURI of {token_id}")
            set_tokenURI(token_id, nft_creator, ipfs_metadata)


def main():
    test = "https://ipfs.io/ipfs/QmNyPc4LYbS3uUkY9YdSc43a2TZFTdUk46URTyLxCwr49m?filename=0-TEST.json"
    set_token_uri(test)
