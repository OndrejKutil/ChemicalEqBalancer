import unittest
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'equationBalancer')))
from balancer import EquationBalancer


class TestEquationBalancer(unittest.TestCase):
    
    balancer = EquationBalancer()

    def test_parseEquation(self):
        self.assertEqual(self.balancer.parseEquation("H2+O2->H2O"), (["H2", "O2"], ["H2O"]))
        self.assertEqual(self.balancer.parseEquation("H2O->H2+O2"), (["H2O"], ["H2", "O2"]))

    def test_emptyEquation(self):
        self.assertEqual(self.balancer.parseEquation(""), ([], []))

    def test_parseMolecule(self):
        self.assertEqual(self.balancer.parseMolecule("C6H12O6"), {'C': 6, 'H': 12, 'O': 6})
        self.assertEqual(self.balancer.parseMolecule("H2O"), {'H': 2, 'O': 1})

    def test_parseMoleculeEmpty(self):  
        self.assertEqual(self.balancer.parseMolecule(""), {})

    def test_getAtoms(self):
        self.assertEqual(self.balancer.getAtoms(["H2", "O2"], ["H2O"]), ['H', 'O'])
        self.assertEqual(self.balancer.getAtoms(["H2O"], ["H2", "O2"]), ['H', 'O'])

    def test_getAtomsEmpty(self):
        self.assertEqual(self.balancer.getAtoms([], []), [])

    def test_buildMatrix(self):
        self.assertEqual(self.balancer.buildMatrix(["H2", "O2"], ["H2O"], ['H', 'O']).tolist(), [[2, 0, -2], [0, 2, -1]])
        self.assertEqual(self.balancer.buildMatrix(["H2O"], ["H2", "O2"], ['H', 'O']).tolist(), [[2, -2, 0], [1, 0, -2]])

    def test_buildMatrixEmpty(self):
        self.assertEqual(self.balancer.buildMatrix([], [], []).tolist(), [])

    def test_balanceEquation(self):
        self.assertEqual(self.balancer.balanceEquation("H2+O2->H2O")[0], "2 H2 + 1 O2 -> 2 H2O")
        self.assertEqual(self.balancer.balanceEquation("H2O->H2+O2")[0], "2 H2O -> 2 H2 + 1 O2")

    def test_balanceEquationEmpty(self):
        self.assertEqual(self.balancer.balanceEquation("")[0], "This equation has no solution")

    


if __name__ == '__main__':
    unittest.main()

