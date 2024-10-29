# import class
from Pen import Pen
from Book import Book
from conta import Conta
from datas import Data

# creating instance of Pen object (object state)
caneta: Pen = Pen('Vermelha', 'Bic', 100, capped=True)

livro = Book('Felicidade Clandestina', 'Clarice Lispector', 1990, closed=True)

d = Data(29, 10, 2024)
print(d.formatada())

#conta_b = Conta(2569, "Babs", 500, 1000)

# conta_b.extrato()
# conta_b.deposito(100)
# conta_b.extrato()
# conta_b.saque(100)
# conta_b.extrato()