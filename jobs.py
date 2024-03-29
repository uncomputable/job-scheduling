from typing import List, Tuple

class Operation:

    def __init__(self, time, machine):
        self.time = time
        self.machine = machine

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if self.time == other.time and self.machine == other.machine:
                return True
        return False

    def __str__(self):
        return "Operation with time " + str(self.time) + " on machine " + str(self.machine)


class Job:

    def __init__(self, operations: List[Operation] = None):
        if operations is None:
            operations = []
        self.operations = operations

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if self.operations == other.operations:
                return True
        return False

    def add_operation(self, op):
        self.operations.append(op)

    def add_operations(self, ops):
        for op in ops:
            self.operations.append(op)

    def __str__(self):
        operations = "Operation"
        times = "Time     "
        machines = "Machine  "
        for i, operation in enumerate(self.operations):
            operations += " " * (7 - len(str(i))) + str(i)
            times += " "*(7 - len(str(operation.time))) + str(operation.time)
            machines += " " * (7 - len(str(operation.machine))) + str(operation.machine)
        return operations + "\n" + times + "\n" + machines
