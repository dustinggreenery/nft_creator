from gc import collect
from metadata.sample_metadata import metadata_template
from customize_nfts import (
    nft_name,
    nft_desc,
    nft_attributes,
    file_type,
    media_type,
    external_url,
    artist,
)
from brownie import NFT_Creator, network
from pathlib import Path
import requests
import json
import os


def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        PINATA_BASE_URL = "https://api.pinata.cloud/"
        endpoint = "pinning/pinFileToIPFS"
        headers = {
            "pinata_api_key": os.getenv("PINATA_API_KEY"),
            "pinata_secret_api_key": os.getenv("PINATA_API_SECRET"),
        }
        filename = filepath.split("/")[-1:][0]
        response = requests.post(
            PINATA_BASE_URL + endpoint,
            files={"file": (filename, image_binary)},
            headers=headers,
        )
        ipfs_hash = response.json()["IpfsHash"]
        file_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print(file_uri)
        return file_uri


def create_metadata():
    metadata_file_name = f"./metadata/{network.show_active()}/0-{nft_name}.json"
    collectible_metadata = metadata_template
    if Path(metadata_file_name).exists():
        print(f"{metadata_file_name} already exists.")
    else:
        print(f"Creating Metadata file: {metadata_file_name}")
        collectible_metadata["name"] = nft_name
        collectible_metadata["description"] = nft_desc
        collectible_metadata["external_url"] = external_url
        attribute_array = []
        for attribute in range(len(nft_attributes)):
            attribute_array.append(
                {
                    "display_type": nft_attributes[attribute][0],
                    "trait_type": nft_attributes[attribute][1],
                    "value": nft_attributes[attribute][2],
                    "max_value": nft_attributes[attribute][3],
                }
            )
        collectible_metadata["attributes"] = attribute_array
        collectible_metadata["artist"] = artist
        image_path = "./file/" + nft_name.lower() + "." + file_type
        image_uri = upload_to_ipfs(image_path)
        collectible_metadata["image"] = image_uri
        collectible_metadata["mediaType"] = media_type + "/" + file_type
        with open(metadata_file_name, "w") as file:
            json.dump(collectible_metadata, file)
        ipfs_metadata = upload_to_ipfs(metadata_file_name)
    return ipfs_metadata


def main():
    create_metadata()
