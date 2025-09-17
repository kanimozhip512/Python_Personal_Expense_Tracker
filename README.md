****# Python Personal Expense Tracker****

A **console-based Python application** to record, view, update, and delete personal expenses.  
This project demonstrates fundamental Python programming concepts including **variables, loops, conditionals, functions, lists, f-strings, and modules**.

---

**## Features**

- ➕ **Add Expenses** with amount, category, and date (defaults to today).  
- 📋 **View Expenses** in a formatted list along with:
  - Total spending  
  - Average expense  
  - Highest expense  
  - A random money-saving tip  
- ✏️ **Update Expenses** by selecting their record number.  
- ❌ **Delete Expenses** by selecting their record number.  
- ✅ **Input validation** ensures correct values (numeric amounts, valid dates, and record selection).  

---

**## How to Run**

1. Clone the repository:

   git clone https://github.com/kanimozhip512/Python_Personal_Expense_Tracker.git
   
2. Navigate into the project folder:

   cd Python_Personal_Expense_Tracker

3. Run the script:
   
  python personal_expense_tracker.py
  
4. Use the menu in your terminal to add, view, update, or delete expenses.

---

****## Sample Output****

--- Personal Expense Tracker ---
1. Add Expense
2. View Expenses
3. Update Expense
4. Delete Expense
5. Exit
Choose an option (1-5): 1

Enter expense amount: ₹250
Enter expense category (Food, Travel, etc.): Food
Enter date (YYYY-MM-DD) or press enter for today:
Expense added: ₹250.0 for Food on 2025-09-17

--- Personal Expense Tracker ---
1. Add Expense
2. View Expenses
3. Update Expense
4. Delete Expense
5. Exit
Choose an option (1-5): 1

Enter expense amount: ₹120
Enter expense category (Food, Travel, etc.): Travel
Enter date (YYYY-MM-DD) or press enter for today:
Expense added: ₹120.0 for Travel on 2025-09-17

--- Personal Expense Tracker ---
1. Add Expense
2. View Expenses
3. Update Expense
4. Delete Expense
5. Exit
Choose an option (1-5): 2

--- Your Expenses ---
1. ₹250.00 | Food   | 2025-09-17
2. ₹120.00 | Travel | 2025-09-17

Total spending: ₹370.00
Average spending: ₹185.00
Highest expense: ₹250.00
💡 Tip: Compare prices before shopping.

--- Personal Expense Tracker ---
1. Add Expense
2. View Expenses
3. Update Expense
4. Delete Expense
5. Exit
Choose an option (1-5): 3

--- Your Expenses ---
1. ₹250.00 | Food   | 2025-09-17
2. ₹120.00 | Travel | 2025-09-17

Total spending: ₹370.00
Average spending: ₹185.00
Highest expense: ₹250.00
💡 Tip: Use cash instead of credit cards to control spending.

Enter the expense number to update: 2
Enter new amount: ₹200
Enter new category: Travel
Enter new date (YYYY-MM-DD) or press enter for today:
Expense updated successfully!

--- Personal Expense Tracker ---
1. Add Expense
2. View Expenses
3. Update Expense
4. Delete Expense
5. Exit
Choose an option (1-5): 2

--- Your Expenses ---
1. ₹250.00 | Food   | 2025-09-17
2. ₹200.00 | Travel | 2025-09-17

Total spending: ₹450.00
Average spending: ₹225.00
Highest expense: ₹250.00
💡 Tip: Save a fixed percentage of your income every month.

--- Personal Expense Tracker ---
1. Add Expense
2. View Expenses
3. Update Expense
4. Delete Expense
5. Exit
Choose an option (1-5): 4

--- Your Expenses ---
1. ₹250.00 | Food   | 2025-09-17
2. ₹200.00 | Travel | 2025-09-17

Total spending: ₹450.00
Average spending: ₹225.00
Highest expense: ₹250.00
💡 Tip: Wait 24 hours before making non-essential purchases.

Enter the expense number to delete: 1
Removed expense: ₹250.0 | Food | 2025-09-17

--- Personal Expense Tracker ---
1. Add Expense
2. View Expenses
3. Update Expense
4. Delete Expense
5. Exit
Choose an option (1-5): 5

Thank you for using the Expense Tracker! 💰

---

**📚 Concepts Practiced**

Variables and data types

Lists and indexing

Conditionals (if, elif, else)

Loops (for, while)

Functions (arguments, return values, scope)

String formatting with f-strings

Modules: random, datetime

Input validation without try/except

