# Budget App 💰📉

An object-oriented command-line application built with Python to track financial categories, manage ledgers, and visualize spending data.

## 🛠️ Technologies Used
* **Python:** Core application logic, string formatting, and mathematical rounding.
* **Object-Oriented Programming (OOP):** Encapsulation of category data, instances, and ledger methods.

## 🗂️ Project Structure
* **`budget-app.py`**: Contains the `Category` class, the `create_spend_chart` visualization function, and the testing data to execute the code.

## 📊 Core Components
The application consists of two main structural parts:
* **`Category`**: Manages distinct budget categories (e.g., Food, Clothing). Handles internal methods for `deposit`, `withdraw`, `get_balance`, `transfer`, and generates a formatted receipt.
* **`create_spend_chart`**: Takes a list of categories, calculates the percentage of total withdrawals per category, and dynamically generates a text-based bar chart.

## 🚀 How to Run
1. Execute the script in your terminal:
   ```bash
   python budget-app.py

## Example Output
```text
*************Food*************
initial deposit        1000.00
groceries               -60.00
Total: 940.0

Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g
