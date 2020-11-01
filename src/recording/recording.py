import datetime

class log:
    '''
    >>> test_log = log()
    >>> assert(test_log.date == datetime.date.today())
    '''

    def __init__(self):
        self.date = datetime.date.today()

