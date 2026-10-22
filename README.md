# Electricity Bill Calculator
## Description
This program calculates the customer's electricity consumption and total bill using their previous and current meter ratings.
## Version 1 - Original code without input validation
- Input: Accepts the customer's name, previous meter reading, and current meter reading.
- Process: Subtracts the previous reading from the current reading to calculate electricity consumption. The consumption is multiplied by PHP 12.90 to calculate the total bill.
- Output: Displays the customer's name electricity consumption, and total bill.
- Does not include input validation.

## Version 2 - Added Input Validation'
Version 2 improves the original program by checking user inputs before calculating the electricity bill.

Validation Rules
1. Customer Name: Must not be empty
2. Previous Meter Reading: Must not be a valid number greater than or equal to 0.
3. Current Meter Reading: Must be a valid number greater than or equal to the previous reading.
4. Error Messages: Displays an error message when invalid input is entered.
5. Input Re-entry: Allows users to enter their information again until it is valid.

Input
- Customer name
- Previous meter reading
- Current meter reading

Process
- Validates the customer's name and meter readings.
- Subtracts the previous reading from the current reading to calculate electricity consumption.
- Multiplies electricity consumption by PHP 12.90 to calculate the total bill.

Output
- Customer name
- Electricity consumption
- Total electricity bill
