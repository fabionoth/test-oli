// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract MobiusMock is ERC20 {
    uint8 private _tokenDecimals;

    constructor() ERC20("Mobius Mock", "MBU") {
        _tokenDecimals = 6; // Real token precision
        _mint(msg.sender, 1_000_000 * (10 ** _tokenDecimals));
    }

    function decimals() public view override returns (uint8) {
        return _tokenDecimals;
    }

    // Vulnerable function: uses 10**18 instead of token.decimals()
    function mintMisscaled(uint256 amt) external {
        uint256 scaled = amt * (10 ** 18); // BUG: ignores token.decimals()
        _mint(msg.sender, scaled);
    }
}