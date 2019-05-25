import logging

# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create formatter
formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

# create filehandler
file_handler = logging.FileHandler('employee.log')
file_handler.setFormatter(formatter)

# add file_handler to logger
logger.addHandler(file_handler)


class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Smith')
emp_2 = Employee('Corey', 'Schafer')
emp_3 = Employee('Jane', 'Doe')