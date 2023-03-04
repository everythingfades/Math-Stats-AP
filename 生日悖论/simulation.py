import random
import argparse
def simulation(people):
    birthdays = list()
    peoples = list()
    for i in range(people):
        birthdays.append(random.randint(1,365))
        peoples.append(i)
    return birthdays,peoples
def tran(z):
    a = [1,31,59,90,120,151,181,212,243,273,304,334]
    str = ''
    for j in z:
        for i in range(len(a)):
            if j < a[i]:
                str += "{}月{}号".format(i,j-a[i-1]+1)
                break
        str += "|"
    return str if str != '' else "无"
def getSame(birthdays):
    cnt = 0
    x = list()
    y = list()
    z = list()
    for i in range(len(birthdays)):
        for j in range(i+1,len(birthdays)):
            if birthdays[i] == birthdays[j]:
                cnt += 1
                x.append(i)
                y.append(j)
                z.append(birthdays[i])
    return cnt,x,y,z

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--num', default=30, type=int, help='人数')
    opt = parser.parse_args()
    birthdays,peoples = simulation(opt.num) #### TODO: alter before use, 可以将括号中数字改为任意整数
    cnt,x,y,z = getSame(birthdays)
    print(tran(birthdays))
    print("有{}组生日相同".format(cnt))
    print("重复日期为" + tran(z))
    for i in range(len(x)):
       print("第{}人和第{}人生日相同".format(x[i]+1,y[i]+1))