from rx import create
from rx.core import Observer

def buy_stock_events(observer, scheduler):
    stocks = [
        {'TCKR': 'APPL', 'PRICE': 200},
        {'TCKR': 'GOOG', 'PRICE': 90},
        {'TCKR': 'TSLA', 'PRICE': 120},
        {'TCKR': 'MSFT', 'PRICE': 230},
        {'TCKR': 'INTL', 'PRICE': 26},
    ]
    for stock in stocks:
        if(stock['PRICE'] > 100):
            observer.on_next(stock['TCKR'])
        # else:
        #     observer.on_error(stock['TCKR'])
    
    observer.on_completed()

source = create(buy_stock_events)



class PrintObserver(Observer):

    def __init__(self):
        super().__init__()
        self.has_on_next = None
        self.has_on_completed = None
        self.has_on_error = None

    def on_next(self, value):
        print("Received {}".format(value))
    
    def on_completed(self):
        print("Done")
    
    def on_error(self):
        print("Error")

source.subscribe(PrintObserver)