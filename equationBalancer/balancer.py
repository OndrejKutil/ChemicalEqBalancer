# import libraries
import re # regular expresion library (built-in)
import numpy as np # numpy for creating matrix
from sympy import Matrix, lcm # Matrix for finding solution to the matrix, lcm for finding least common multiple if the solution is in fractions

class EquationBalancer:
    def __init__(self):
        pass

    def parseEquation(self, equation: str) -> tuple:
        """
        split the equation into reactants (left side) and products (right side)\n
        eg.: parseEquation("H2+O2->H2O") return (["H2", "O2"], ["H2O"])
        """
        try:
            reactants, products = equation.replace(' ', '').split('->')
            reactants = reactants.split('+')
            products = products.split('+')

            return reactants, products
        except Exception:
            raise Exception('Invalid equation')

    def parseMolecule(self, molecule: str) -> dict:
        """
        counts how many times an atom is present inside given molecule\n
        eg.: C6H12O6 -> {'C': '6', 'H': '12', 'O': '6'}
        """
        
        # returns dict with atom and it's count in the molecule
        # [A-Z] - upper case followed by any number of lowecase symboles (denoted by star behind [a-z])
        # (\d*) gives the number behind the string explained above, eg.: "H2" -> gives the 2
        # re.findall() return a tuple
        # r in front of a string means a raw string
        # doesnt treat backslashes as an escape characters (eg. \n for new line or \t for tab)
        atomPatternRe = r'([A-Z][a-z]*)(\d*)'
        parsedMolecule = re.findall(atomPatternRe, molecule)

        # creates a dictionary with atoms and its count in the molecule
        atomCounts = {}
        for atom, count in parsedMolecule:
            count = int(count) if count else 1 # else 1 because re.findall() gives empty string ('') when atom is present only once
            if atom in atomCounts:
                atomCounts[atom] += count
            else:
                atomCounts[atom] = count

        return atomCounts

    def getAtoms(self, reactants: list, products: list) -> list:
        """
        eg.: H2+O2->H2O returns ["H", "O"]
        """
        atoms = set()
        for molecule in reactants + products:
            # adds the atom to the set (.update())
            # parseMolecule(x) gives me the eg. dict: {"H": "2"} so the .keys() gives us only the keys - eg.: {"H": "2"} -> "H"
            atoms.update(self.parseMolecule(molecule).keys())

        # returns list instead of set (easier to work with)
        return sorted(atoms)

    def buildMatrix(self, reactants: list, products: list, atoms: list) -> list[list[int]]:
        """
        Builds matrix from given equation
        """
        # gets how many atoms are present in given equation
        numAtoms = len(atoms)
        # how many molecules are in given equation
        numMolecules = len(reactants) + len(products)

        # creates a matrix with rows = to how many atoms are in an equation and columns = to how many molecules are in an equation
        # all 0s, all elements are int (dtype = int), else all elements would look like: 0. (. signaling it is a float (meaning 0.0))
        matrix = np.zeros((numAtoms, numMolecules), dtype=int)

        for j, molecule in enumerate(reactants + products): # gives count (index j) and the coresponding value in the list
            atomCounts = self.parseMolecule(molecule)
            for i, atom in enumerate(atoms):
                
                # if j >= len(reactants) means that we are on the product side, thus need to multiply the count by -1
                # .get(key, default value)
                matrix[i, j] = atomCounts.get(atom, 0) * (-1 if j >= len(reactants) else 1)

        return matrix

    def generateFinalSolutionString(self, reactants: list, products: list, solution: list) -> str:
        """
        Generates final solution string from given equation and solution list
        """
        solutionString = ''

        for i in range(len(reactants)):
            solutionString = solutionString + f'{solution[i]} {reactants[i]}' + ' + '

        solutionString = solutionString.rstrip(' + ')
        solutionString = solutionString + ' -> '

        for i in range(len(products)):
            solutionString = solutionString + f'{solution[i + len(reactants)]} {products[i]}' + ' + '

        solutionString = solutionString.rstrip(' + ')
            
        return solutionString

    def balanceEquation(self, equation: str) -> tuple:
        """
        Balances given chemical equation using previously defined functions

        returns tuple with solution string and exit code, if exit code = 0, then the solution is correct, else it = 1, it is an error
        """

        # try/except is used to catch any errors that may occur
        try:
            reactants, products = self.parseEquation(equation)
            atoms = self.getAtoms(reactants, products)
            matrix = self.buildMatrix(reactants, products, atoms)

            # using sympy we can find the null space (= the solution)
            nullSpace = Matrix(matrix).nullspace()
            if not nullSpace:
                return 'This equation has no solution', 1
            else:
                solution = nullSpace[0]

            # the solution may be in non-integer form, ie fraction
            # we need to convert it to integers
            # in sympy the denominator of a number is in .q
            denominators = [number.q for number in solution]
            # finds least common multiple of the denominators
            lcmDenominator = lcm(denominators)

            integerSolution = [number * lcmDenominator for number in solution]

            # with solution or error returns an exit code, so that we know if the messge in the first element of the tuple is an error or not
            return self.generateFinalSolutionString(reactants, products, integerSolution), 0
        except Exception as e:
            return f'Error: {e}', 1
