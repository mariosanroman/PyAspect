#
import copy
from ..entities.Entity import Entity

#
class AspectException(BaseException):
    pass
#
class Engine:
    def __init__(self, args=None):
        self.store = None #args.store if args.store else None #Store()
        self.target = "PythonMemoryModel"
        self.aqlEngine = None #AqlEngine()

    #
    @staticmethod
    def copy_properties(source, target, deep=False):
        Entity.copy_properties(source, target, deep)

    #
    def getOperationImpl(self, args):
        #operation = self.getOperation(args);
        #return Engine.newInstance(operation.localFullName, args);
        raise NotImplementedError()

    #
    def get_operation(self, args):
        raise NotImplementedError()

    #
    def query(self, q):
        # return self.aqlEngine.execute(q)
        raise NotImplementedError

    #
    def register(metadata, clazz):
        raise NotImplementedError
        