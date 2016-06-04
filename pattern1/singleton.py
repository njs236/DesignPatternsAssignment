class Singleton(object):
    @classmethod
    def Instance(cls, *args, **kwargs):
        self = "__self__"
        if not hasattr(cls, self):
            instance = object.__new__(cls)
            instance.init(*args, **kwargs)
            setattr(cls, self, instance)
        return getattr(cls, self)

    def init(self, *args, **kwargs):
        pass



class SingletonManager(object):
    def __init__(self):
        self.name = "SingletonManager"
        self.dict = {}

    def Register(self, object, name):
        if name not in self.dict:
            self.dict[name] = object

    def Get(self, name):
        try:
            return self.dict[name]
        except (IndexError):
            print("No such class")
