// Replace the following values with the actual data from your transaction
const txCount = 10;
const txTime = "2024-01-05 11:05:08";
const txFees = 27_504;
const confirmations = 15;
const miner = "example_miner";

// Update the HTML content with the extracted information
document.getElementById("txCount").innerText = txCount;
document.getElementById("txTime").innerText = txTime;
document.getElementById("txFees").innerText = txFees;
document.getElementById("confirmations").innerText = confirmations;
document.getElementById("miner").innerText = miner;
