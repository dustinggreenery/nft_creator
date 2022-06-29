// SPDX-License-Identifier: MIT

pragma solidity 0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract NFT_Creator is ERC721 {
    string private tokenName = "Datapack Test";
    string private tokenSymbol = "DT";
    uint256 public tokenCounter;

    constructor() public ERC721(tokenName, tokenSymbol) {
        tokenCounter = 0;
    }

    function createCollectible() public returns (bytes32) {
        address owner = msg.sender;
        uint256 newTokenId = tokenCounter;
        _safeMint(owner, newTokenId);
        tokenCounter = tokenCounter + 1;
    }

    function setTokenURI(uint256 tokenId, string memory _tokenURI) public {
        require(
            _isApprovedOrOwner(_msgSender(), tokenId),
            "ERC721: caller is not owner no approved"
        );
        _setTokenURI(tokenId, _tokenURI);
    }
}
