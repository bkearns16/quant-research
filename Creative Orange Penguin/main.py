from AlgorithmImports import *

# version control test
class BasicTemplateAlgorithm(QCAlgorithm):

    def initialize(self):
        self.set_start_date(2020, 1, 1)
        self.set_end_date(2020, 2, 1)
        self.set_cash(100000)

        self.add_equity("QQQ", Resolution.DAILY)

    def on_data(self, data: Slice):
        if not self.portfolio.invested:
            self.set_holdings("QQQ", 1)
