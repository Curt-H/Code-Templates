from time import localtime, strftime


def log(*args, **kwargs):
    t = localtime()
    st = strftime('%Y-%m-%d %I:%M:%S', t)

    print(f'[{st}]')
    print('=' * 50)
    print(*args)
    print('-' * 50)
    for k in kwargs.keys():
        print(f'{k}={kwargs[k]}')
    print('=' * 50, end='\n\n')

    with open('log.txt', 'a+', encoding='utf-8') as f:
        print(f'[{st}]', file=f)
        print('=' * 50, file=f)
        print(*args, file=f)
        print('-' * 50, file=f)
        for k in kwargs.keys():
            print(f'{k}={kwargs[k]}', file=f)
        print('=' * 50, end='\n\n', file=f)


if __name__ == '__main__':
    for i in range(10):
        log('test')
    print(localtime())
