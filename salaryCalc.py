from breezypythongui import EasyFrame

class SalaryCalculator(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Salary Calculator", width=300, height=200, background="#f0f0f0")

        # Hourly wage label and entry
        self.addLabel("Hourly Wage:", 0, 0, background="#f0f0f0", sticky="E")
        self.hourlyWageField = self.addFloatField(0.0, 0, 1, sticky="W")

        # Hours worked label and entry
        self.addLabel("Hours Worked:", 1, 0, background="#f0f0f0", sticky="E")
        self.hoursWorkedField = self.addFloatField(0.0, 1, 1, sticky="W")

        # Calculate button
        self.calculateButton = self.addButton("Calculate Salary", 2, 0, columnspan=2, command=self.calculateSalary)
        self.calculateButton.configure(background="#367c2b", foreground="white")

        # "Your Salary is:" label
        self.addLabel("Your Salary is:", 3, 0, columnspan=2, sticky="S", background="#f0f0f0", font=("Arial", 12))

        # Result label
        self.resultLabel = self.addLabel("", 4, 0, columnspan=2, sticky="S", background="#f0f0f0", font=("Arial", 12))

        # Center all columns
        for i in range(2):
            self.columnconfigure(i, weight=1)

        # Center all rows
        for i in range(5):
            self.rowconfigure(i, weight=1)

    def calculateSalary(self):
        # Get values from the entry fields
        hourly_wage = self.hourlyWageField.getNumber()
        hours_worked = self.hoursWorkedField.getNumber()

        # Calculate salary
        salary = hourly_wage * hours_worked

        # Update the result label
        self.resultLabel["text"] = f"${salary:.2f}"

if __name__ == "__main__":
    salary_calculator = SalaryCalculator()
    salary_calculator.mainloop()