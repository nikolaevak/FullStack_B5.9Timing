
import time
#декоратор секундомер
def time_this(num_runs):
    def time_decorator(func):
        import time
        def wrapper(*args, **kwargs):
            avg_time = 0
            for _ in range(num_runs):
                t0 = time.time()
                return_value = func(*args, **kwargs)
                t1 = time.time()
                avg_time += (t1-t0)
            print('[*] Среднее время выполнения: {} секунд.'.format(avg_time / num_runs))
            return return_value
        return wrapper
    return time_decorator

@time_this(num_runs=10)
def f():
    for j in range(1000000):
        pass

#класс секундомер
class Time_this:
    def __init__(self,func):
        self.num_runs = 10 # атрибут статичный
        self.function = func #атрибут динамический

    def __call__(self, *args, **kwargs): # делает вызов экземпляра
        avg_time = 0
        for _ in range(self.num_runs):
            t0 = time.time()
            self.function(*args, **kwargs)
            t1 = time.time()
            avg_time += (t1 - t0)
        print('[*] Среднее время выполнения: {} секунд.'.format(avg_time / self.num_runs))
        return self.function(*args, **kwargs)

@Time_this
def f():
    for j in range(1000000):
        pass
