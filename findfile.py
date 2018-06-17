# -*- coding:utf-8 -*-
import os

def foundfiles(key,search_path):
    foundlist = []
    for path,dirs,files in os.walk(search_path):
        print 'searching',path,'...'
        for name in files:
            full_name = path + '/' + name
            if key in name:
                foundlist.append(full_name)
            with open(full_name) as f:
                for line in f.readlines():
                    if key in line:
                        foundlist.append(full_name+':'+line)
    return foundlist


if __name__ == '__main__':
    key = raw_input("input key: ")
    path = raw_input("input path: ")
    if not path.split():
        path = '.'
    result = foundfiles(key, path)
    print '\n========================= results ================================\n'
    for r in result:
        print r