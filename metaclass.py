class Single(type):
    _count_cls = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._count_cls:
            cls._count_cls[cls] = super(
                Single, cls).__call__(*args, **kwargs)
        return cls._count_cls[cls]


class Work(metaclass=Single):
    def __init__(self):
        print('\nРаботаем!!!')


worker1 = Work()
worker2 = Work()
print(worker1 == worker2)
print(Single._count_cls)
