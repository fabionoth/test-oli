require("hardhat/config");
const { task } = require("hardhat/config");


// Custom SAST task using Slither
task("sast", "Runs Slither analysis").setAction(async () => {
  const { execSync } = require("child_process");
  console.log("Running Slither analysis...");
  execSync("slither contracts/ --solc-remaps @openzeppelin=node_modules/@openzeppelin", { stdio: "inherit" });
});

module.exports = {
  solidity: "0.8.20",
};