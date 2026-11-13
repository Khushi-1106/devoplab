def div(a,b):
  return a/b
def subtract(a,b):
  return a-b
def multipy(a,b):
  return a*b

class TestCalculator(unittest,TestCase):
  def test_div(self):
    self.assert.Equal(add(30,20),40)
  def test_subtract(self):
    self.assertEqual(subtract(20,10),10)
  def test_multiply(self):
    self.assertEqual(multiply(6,4),24)
    
if __name__ == "__main__":
  print("Student calculator application")
  print("addition",div(20,20))
  print("subtraction:",subtract(20,10))
  print("multiplication:",multiply(5,4))
  print("\n excecuting automated tests....\n")
  unittest.main(argv=['first-srg-is-ignored'],exit=false)
