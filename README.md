
## Project Structure

- `contracts/`: Contains the Solidity smart contracts.
- `scripts/`: Contains scripts for deployment and other tasks.
- `test/`: Contains test files for the smart contracts.
- `hardhat.config.js`: Configuration file for Hardhat.
- `slither.config.json`: Configuration file for Slither (if applicable).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/fabionoth/test-oli
   cd test-oli
   ```

2. Install dependencies:
   ```bash
   npm install
   npm run compile 
   cp decimal_mismatch_detector.py  ~/.local/lib/python3.10/site-packages/slither/detectors/
   slither contracts/ --solc-remaps @openzeppelin=node_modules/@openzeppelin --detect decimal-mismatch
   ```

3. Run the project:

## Troubleshooting

- Ensure all dependencies are installed correctly.
- Verify that the correct versions of Node.js, npm, Python, and pip are installed.
- Check file permissions if you encounter permission errors.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.