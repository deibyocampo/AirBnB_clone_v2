#!/usr/bin/python3
'''
script that deletes out-of-date archives, using the function do_clean:
'''
from fabric.api import run, env, hosts


env.hosts = ['35.243.213.140', '34.73.54.82']
env.user = 'ubuntu'


def do_clean(number=0):
    ''' delete old archive files '''
    if number == 0:
        number = number + 2
    number = number + 1
    result = local('ls -t /versions | tail -n +number| xargs rm')
    if result.failed:
        return False
    result = run('ls -t /data/web_static/releases | tail -n +number| xargs rm')
    if result.failed:
        return False

    return True
