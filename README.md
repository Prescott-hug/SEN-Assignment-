The Personal Expense Tracker is a Python command-line application that allows
users to record, view, and analyze daily expenses. The application stores data
in a JSON file for persistence.

--------------------------------------------------
SOFTWARE DEVELOPMENT LIFE CYCLE (SDLC)
--------------------------------------------------

1. REQUIREMENT ANALYSIS
- Users need to track daily expenses.
- The system should categorize expenses.
- Total spending must be calculated automatically.
- Expense records must be saved for future use.

2. PLANNING
- Python chosen for rapid development.
- JSON file selected for data storage.
- CLI-based menu interface planned.

3. DESIGN
- Expense data structure includes:
  • Amount
  • Category
  • Date
  • Note
- Modular functions handle each operation.

4. DEVELOPMENT
- Python features used:
  • File handling
  • datetime module
  • Exception handling
- Code written using structured programming.

5. TESTING
- Tested adding valid and invalid expense values.
- Verified total expense calculations.
- Ensured file persistence after program restart.

6. DEPLOYMENT
- Application executed locally using:
  python expense_tracker.py
- No third-party libraries required.

7. MAINTENANCE
- Possible future improvements:
  • Monthly expense reports
  • Graphical charts
  • CSV export functionality
  • Mobile or web version
