# Nike Warehouse Inventory Management System

## Description
This Python program helps a Nike warehouse store manager manage and analyse stock-taking data. It provides an overview of inventory items and supports basic stock management operations to improve organisation and delivery efficiency.

## Inventory Data
Each stock item in the system includes the following information:
- Country
- Product Code
- Product Name
- Cost per Unit
- Quantity in Stock
- Total Value (calculated as cost × quantity)

Inventory data is stored in a text file and loaded into the program at runtime.

## Features
- Search for products using a unique product code
- Identify the product with the lowest quantity and restock it
- Identify the product with the highest quantity in stock
- Calculate and display the total value of each stock item
- Console-based menu for easy interaction

## Requirements
- Python 3.x
- Any code editor (VS Code, PyCharm, IDLE, etc.)

## How to Run
1. Open the project in your preferred code editor.
2. Ensure `inventory.txt` is in the same directory as `inventory.py`.
3. Run the program:
   ```bash
   python inventory.py
