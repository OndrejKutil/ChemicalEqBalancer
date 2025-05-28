# ⚗️ Chemical Equation Balancer

[![MIT License](https://img.shields.io/github/license/OndrejKutil/ChemicalEqBalancer?style=for-the-badge)](./LICENSE)  
A Python program that parses and balances unbalanced chemical reactions using matrix algebra. Built as a university project, it combines string parsing, regex, and linear algebra to automate a classic chemistry task.

---

## 📌 Project Description

This project balances chemical equations automatically by:
- **Parsing** the equation into atomic components
- **Analyzing** atom counts for each compound
- **Building** and solving a matrix system to determine stoichiometric coefficients

It’s a clean example of applying computer science fundamentals (regex, matrices, systems of equations) to solve a real-world problem from chemistry.

---

## 🧠 Skills Demonstrated

- **Regex-based Parsing:** Extracting element counts and molecule structures from raw input strings
- **Matrix Algebra:** Building and solving coefficient matrices using NumPy
- **Edge Case Handling:** Validating chemical notation, handling already-balanced inputs, and reducing fractions
- **Test-Driven Development:** Ensuring correctness with multiple unit test cases

---

## 🧪 Example Inputs & Outputs

```bash
Input:    H2 + O2 -> H2O
Output:   2 H2 + O2 -> 2 H2O

Input:    Cl2 + H2 -> HCl
Output:   Cl2 + H2 -> 2 HCl

Input:    C3H8 + O2 -> CO2 + H2O
Output:   C3H8 + 5 O2 -> 3 CO2 + 4 H2O
```

---

## ⚙️ How It Works
1. Parsing Stage:
Uses regular expressions to extract atoms and counts from compounds on both sides of the reaction.

2. Matrix Setup:
Each element becomes a row in a system of linear equations. Each molecule becomes a column. A matrix is built representing atom counts across reactants and products.

3. Solving Stage:
Applies NumPy’s linear algebra tools to solve the system and compute the smallest integer coefficients that balance the equation.

4. Formatting Stage:
Outputs a clean, readable balanced equation.

---

## 📁 File Structure

```bash
📦ChemicalEqBalancer
 ┣ 📁Docs                # docs
 ┃ ┣ 📜main.py           # app entry point
 ┃ ┗ 📜balancer.py       # main balancer file   
 ┣ 📁Tests               # test
 ┗ 📁equationBalancer    # main app  
```
