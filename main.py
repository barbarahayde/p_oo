# import class
from Pen import Pen
from Book import Book

# creating instance of Pen object (object state)
caneta: Pen = Pen('Vermelha', 'Bic', 100, capped=True)

livro = Book('Felicidade Clandestina', 'Clarice Lispector', 1990, closed=True)

caneta.get_color()