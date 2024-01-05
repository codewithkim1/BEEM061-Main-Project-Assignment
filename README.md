# BEEM061 Main Assignment Part B

## Abstract
The main assignment for BEEM061 comprises two equally weighted parts: Part A - a 1,500 word essay, and Part B - a technical task-based assignment contributing 40% to the overall module grade. This document outlines the tasks for Part B.


### 1. Explore the Bitcoin Blockchain and Basic Web Coding (30 marks)

#### 1.1 Extract Information From Your Own Transaction (15 marks)

At the beginning of the module, participants set up Handcash Wallets and completed a survey that paid micropayments automatically. For this task:

- Go to your transaction history and locate a transaction on the blockchain.
- Note the block height of the transaction.
- From a Jupyter notebook, use the whatsonchain API to extract information from the specified block.
    - Data to fetch: txcount, time, totalFees, confirmations, miner.
    - Convert the Unix timestamp into human-readable format.

Explain the significance of each extracted part of the block.

#### 1.2 Basic Web Coding (15 marks)

Refer to the Wallet workshop materials on satolearn.com. Create a web page that:

1. Generates a random private key (not shown on the webpage).
2. Constructs a corresponding public key and address.
3. Generates a QR code for receiving money.
4. Includes a link to live information from an API service (e.g., cryptocurrency price) on the wallet website.

### 2. Time Series Investigation of Bitcoin Price (45 marks)

#### 2.1 Obtain Time Series Data (5 marks)

Call the FRED API (or another of your choice) from a Jupyter notebook to obtain time series data for:
1. Chosen cryptocurrency/high-risk stock.
2. Chosen safe asset (e.g., stock of a large company).
3. Overall stock market performance (e.g., S&P500).

Provide clear labels for the three series in your time series plots.

#### 2.2 Data Transformations (10 marks)

- Use the longest possible time span for analysis.
- Combine the three data series into a Pandas DataFrame with compatible time periods.
- Transform observations into returns using the specified formula.

#### 2.3 Data Analysis (30 marks)

Determine the correlation between returns on risky and safe assets and market returns. Interpret the results with respect to CAPM theory. Estimate α and β for the chosen risky asset using OLS regression and interpret the results.

### 3. Machine Learning in Practice (25 marks)

Refer to the provided repository and the 'model' folder for Python modeling.

#### 3.1 High Level Description of FinTech Firm (10 marks)

Provide a mechanical description of Sarunas’ FinTech firm, explaining the four structural parts, their interactions, and overall achievements. Include a description of Logistic Regression and its usefulness in machine learning.

#### 3.2 Written Description of Python Code (10 marks)

Reproduce Sarunas’ model within your Jupyter notebook, following instructions to download the dataset from Kaggle. Choose 10 lines of code, include brief verbal descriptions of their functions, and save as your own Jupyter notebook (excluding the dataset).

#### 3.3 Build your own Machine Learning Model (5 marks)

Choose a dataset and machine learning model within the realm of financial prediction. Utilize the Scikit library and explore predictions with financial data.

## Submission Guidelines

- Submit your assignment as a set of documents with separate Jupyter notebooks (.ipynb extension).
- Optionally, store your code on your own GitHub repository or elsewhere.
- Ensure clear documentation and explanation of your code and results.


