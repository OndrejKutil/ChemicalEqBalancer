# import libraries
import re #re is a regular expresion library



def welcomeMessage():    
    # print welcome screen
    print("Automatic chemical equation balancer")
    print("Input should look similar to this: H2+Cl2->HCl")
    print("Input is case sensitive")
    eq = input("Input: ")
    return eq


def parseEquation(equation: str) -> tuple:
    """
    split the equation into reactants (left side) and products (right side)\n
    eg.: parseEquation("H2+O2->H2O") return (["H2", "O2"], ["H2O"])

    Args:
        equation (str): string form of the equation

    Returns:
        tuple (reactants, products):
    """
    reactants, products = equation.split('->')
    reactants = reactants.split('+')
    products = products.split('+')

    # eg.: parseEquation("H2+O2->H2O") return (["H2", "O2"], ["H2O"])
    return reactants, products


def parseMolecule(molecule: str) -> dict:
    """
    counts how many times an atom is present inside given molecule\n
    eg.: C6H12O6 -> [('C', '6'), ('H', '12'), ('O', '6')]

    Args:
        molecule (str):
    
    Returns:
        dict: dictionary containing atoms and their count
    """
    
    # returns list containing tuples with atom and it's count in the molecule, eg.: C6H12O6 -> [('C', '6'), ('H', '12'), ('O', '6')]
    # [A-Z] - upper case followed by any number of lowecase symboles (denoted by star behind [a-z])
    # (\d*) gives the number behind the string explained above, eg.: "H2" -> gives the 2
    atomPatternRe = r'([A-Z][a-z]*)(\d*)'
    parsedMolecule = re.findall(atomPatternRe, molecule)

    # creates a dictionary with atoms and its count in the molecule
    atomCounts = {}
    for atom, count in parsedMolecule:
        count = int(count) if count else 1
        if atom in atomCounts:
            atomCounts[atom] += count
        else:
            atomCounts[atom] = count

    return atomCounts


def getAtoms(react: list, prod: list) -> list:
    atoms = set()
    for molecule in react + prod:
        atoms.update(parseMolecule(molecule=molecule).keys())

    return sorted(atoms)

