# -*- coding:utf-8 -*-

#读取成绩单
with open('report.txt') as f:
    report_list = [l.split() for l in f.readlines()]
#统计个人总成绩和平均分,插入分数行
for score_line in range(1,len(report_list)):
    total_score = 0
    for score in range(1,len(report_list[score_line])):
        total_score += float(report_list[score_line][score])
    aver_score = float('%.1f' % (total_score / len(report_list[score_line]) - 1))
    report_list[score_line].append(str(total_score))
    report_list[score_line].append(str(aver_score))
#按平均分排序
report_list.sort(key = lambda x:x[-1],reverse = True)
#汇总每一科目的平均分和总平均分
aver_line = []
for subject in range(1,len(report_list[1])):
    total_subject = 0
    for student in range(1,len(report_list)):
        total_subject += float(report_list[student][subject])
    aver_subject = float('%.1f' % (total_subject / (len(report_list) - 1)))
    aver_line.append(str(aver_subject))
aver_line.insert(0, '0')
aver_line.insert(1,'平均')
report_list.insert(1,aver_line)
#添加名次，标记不及格
for score_line in range(2,len(report_list)):
    report_list[score_line].insert(0,str(score_line - 1))
    for score in range(2, (len(report_list[score_line]) - 2)):
        if float(report_list[score_line][score]) < 60:
            report_list[score_line][score] = '不及格'
#添加标题行
report_list[0].insert(0,'名次')
report_list[0].append('总分')
report_list[0].append('平均分')
for line in report_list:
    print ' '.join(line)
#写入新文件
with open('newreport.txt','w') as f:
    for line in report_list:
        f.write('\t'.join(line) + '\n')