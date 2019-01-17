'''
Created on 2019_1_17

@author: wkn
'''
import time

def extimer(f):
    def fi(*args, **kwargs):
        start = time.clock()
        res = f(*args, **kwargs)
        print('--> RUN TIME: <%s> : %s' % (f.__name__, time.clock() - start))
        return res
    return fi

@extimer
def _test1():
    print('work is running')
    time.sleep(3)
    print('workinig done')

if __name__ == '__main__':
    _test1()