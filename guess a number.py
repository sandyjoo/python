# -*- coding:utf-8 -*-

import random


def input_number():     #判断输入合法性
    while True:
        x = raw_input('请输入10以内的整数：\n')
        if x.isdigit():
            if int(x) <= 10:
                break
        else:
            continue
    return int(x)


def guess_num(secret):      #猜数字，返回猜中的次数
    times = 0
    while True:
        times += 1
        print '第 %d 次' % times
        guess = input_number()
        if guess > secret:
            print '%d 太大了' % guess
        elif guess < secret:
            print '%d 太小了' % guess
        else:
            print '猜中了！答案就是 %d' % guess
            break
    print '你猜中答案一共用了 %d 次机会' % times
    return times


def save_name(records,name):        #判断记录是否存在，如果不存在，则追加记录，同时，返回记录的行数
    if len(records) == 1:
        records.append([name,'0','0','0',''])
        print "欢迎 %s ，祝你游戏愉快！" % name
        return 1
    else:
        for i in range(1,len(records)):
            if records[i][0] == name:
                print "欢迎回来 %s ，祝你游戏愉快！" % name
                return i
        records.append([name,'0','0','0',''])
        print "欢迎 %s ，祝你游戏愉快！" % name
        return len(records) - 1



if __name__ == '__main__':
    with open('guess a number.txt') as f:       #打开已有记录的文件，标题行“name	rounds	aver_score	min_score	score_list”
        records = [l.split('\t\t') for l in f.readlines()]
    #print records
    player = raw_input("input your name: ")
    line = save_name(records,player)
    #print line
    while True:
        rounds = int(records[line][1]) + 1
        print "================= ROUND %d ====================" % rounds
        secret = random.randint(1, 10)      #产生随机数
        score = guess_num(secret)           #猜数字，得到猜中的次数
        score_list = [int(i) for i in records[line][4].split()]
        score_list.append(score)
        aver_score = float('%.1f' % (float(sum(score_list)) / rounds))
        records[line][1] = str(rounds)              #记录玩的次数
        records[line][2] = str(aver_score)          #记录猜中的平均成绩
        records[line][3] = str(min(score_list))     #记录猜中的最好成绩
        score_list = [str(i) for i in score_list]
        records[line][4] = ' '.join(score_list) + '\n'      #记录每次猜中的次数
        print '''你一共玩了 %s 次游戏
你平均 %s 次猜中答案
你最好成绩是 %s 次    
        ''' % (records[line][1], records[line][2], records[line][3])
        answer = raw_input('输入\"go\"再玩一次，否则退出游戏\n')
        if answer != 'go':
            print '游戏结束！'
            with open('guess a number.txt','w') as w:       #所有记录写文件
                for line in records:
                    print line
                    w.write('\t\t'.join(line))
            break
        else:
            print '新的一轮'


