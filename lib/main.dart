import 'package:flutter/material.dart';

void main() {
  runApp(const BudgetApp());
}

class BudgetApp extends StatelessWidget {
  const BudgetApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Budget Tracker',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const BudgetHomePage(),
    );
  }
}

class BudgetHomePage extends StatefulWidget {
  const BudgetHomePage({super.key});

  @override
  State<BudgetHomePage> createState() => _BudgetHomePageState();
}

class _BudgetHomePageState extends State<BudgetHomePage> {

  final TextEditingController incomeController = TextEditingController();
  final TextEditingController expenseNameController = TextEditingController();
  final TextEditingController expenseAmountController = TextEditingController();

  double income = 0;
  double totalExpenses = 0;

  List<Map<String, dynamic>> expenses = [];

  void setIncome() {
    setState(() {
      income = double.tryParse(incomeController.text) ?? 0;
    });
  }

  void addExpense() {
    String name = expenseNameController.text;
    double amount =
        double.tryParse(expenseAmountController.text) ?? 0;

    if (name.isEmpty || amount <= 0) {
      return;
    }

    setState(() {
      expenses.add({
        'name': name,
        'amount': amount,
      });

      totalExpenses += amount;
    });

    expenseNameController.clear();
    expenseAmountController.clear();
  }

  double get remainingBalance {
    return income - totalExpenses;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(

      appBar: AppBar(
        title: const Text("💸 Budget Tracker"),
        centerTitle: true,
      ),

      body: Padding(
        padding: const EdgeInsets.all(20),

        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [

            // BALANCE CARD
            Container(
              width: double.infinity,
              padding: const EdgeInsets.all(20),
              decoration: BoxDecoration(
                color: Colors.blue,
                borderRadius: BorderRadius.circular(20),
              ),

              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [

                  const Text(
                    "Remaining Balance",
                    style: TextStyle(
                      color: Colors.white70,
                      fontSize: 18,
                    ),
                  ),

                  const SizedBox(height: 10),

                  Text(
                    "\$${remainingBalance.toStringAsFixed(2)}",
                    style: const TextStyle(
                      color: Colors.white,
                      fontSize: 32,
                      fontWeight: FontWeight.bold,
                    ),
                  ),

                  const SizedBox(height: 10),

                  Text(
                    "Income: \$${income.toStringAsFixed(2)}",
                    style: const TextStyle(color: Colors.white),
                  ),

                  Text(
                    "Expenses: \$${totalExpenses.toStringAsFixed(2)}",
                    style: const TextStyle(color: Colors.white),
                  ),
                ],
              ),
            ),

            const SizedBox(height: 25),

            // INCOME INPUT
            TextField(
              controller: incomeController,
              keyboardType: TextInputType.number,
              decoration: InputDecoration(
                labelText: "Monthly Income",
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(15),
                ),
              ),
            ),

            const SizedBox(height: 10),

            ElevatedButton(
              onPressed: setIncome,
              child: const Text("Set Income"),
            ),

            const SizedBox(height: 25),

            // EXPENSE NAME
            TextField(
              controller: expenseNameController,
              decoration: InputDecoration(
                labelText: "Expense Name",
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(15),
                ),
              ),
            ),

            const SizedBox(height: 10),

            // EXPENSE AMOUNT
            TextField(
              controller: expenseAmountController,
              keyboardType: TextInputType.number,
              decoration: InputDecoration(
                labelText: "Expense Amount",
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(15),
                ),
              ),
            ),

            const SizedBox(height: 10),

            ElevatedButton(
              onPressed: addExpense,
              child: const Text("Add Expense"),
            ),

            const SizedBox(height: 25),

            const Text(
              "Expenses",
              style: TextStyle(
                fontSize: 22,
                fontWeight: FontWeight.bold,
              ),
            ),

            const SizedBox(height: 10),

            // EXPENSE LIST
            Expanded(
              child: ListView.builder(
                itemCount: expenses.length,

                itemBuilder: (context, index) {

                  return Card(
                    margin: const EdgeInsets.only(bottom: 10),

                    child: ListTile(
                      leading: const Icon(Icons.attach_money),

  title: Text(
    expenses[index]['name'],
  ),

  trailing: Row(
    mainAxisSize: MainAxisSize.min,
    children: [

      Text(
        "\$${expenses[index]['amount'].toStringAsFixed(2)}",
      ),

      IconButton(
        icon: const Icon(Icons.delete, color: Colors.red),

        onPressed: () {

          setState(() {

            totalExpenses -= expenses[index]['amount'];

            expenses.removeAt(index);

          });

        },
      ),
    ],
  ),
                    ),
                  );
                },
              ),
            ),
          ],
        ),
      ),
    );
  }
}