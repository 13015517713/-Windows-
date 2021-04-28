import json
import csv
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import numpy as np

# 解析json并画图
def getData():
    fp = open('C:/Users/24302/Desktop/毕设安排/项目相关/GraduationProject-Toolcode-Windows/images/instance_11_job_95482325353/instance_11_job_95482325353.json', 'r')
    data = json.load(fp)
    # 按照starttime排序
    time2Data = {} # 时间字符串到数据的对应，因为我会按照开始时间排序
    for metric in data:
        time2Data[metric['start_time']] = metric
    sortedData = sorted([int(i) for i in time2Data])
    sortedData = [str(i) for i in sortedData]
    # 写入文件
    
    Y = []
    baseTime = int(time2Data[sortedData[0]]['start_time'])
    for i,stime in enumerate(sortedData):
        metric = time2Data[stime]
        # micsec = int(metric['start_time']) - baseTime
        Y.append(float(metric['average_usage']['cpus']) )

    # Y压缩下，每次算一个小时的平均值
    # newY = []
    # for i in range(0,len(Y), 12):
    #     if i+12 <= len(Y):
    #         newY.append(sum(Y[i:i+12]) / 12 )
    #     else:
    #         newY.append(sum(Y[i:]) / len(Y[i:]) )
    # Y = newY
    # X = np.arange(len(Y))
    fp = open("cpu_ave.csv", "w", newline='')
    writer = csv.writer(fp)
    for i,stime in enumerate(sortedData):
        metric = time2Data[stime]
        writer.writerow([metric['average_usage']['cpus']])


    # 用svm训练，看下准确率

    # 画图
    # plt.figure(1)
    # plt.subplot()
    # plt.plot(X,Y,label='instance_755')
    # plt.title("LcTask load waves")
    # plt.xlabel("realtive_time/h")
    # plt.ylabel("cpu_usage")
    # ax = plt.gca()
    # # x_major_locator=MultipleLocator(12)
    # # y_major_locator=MultipleLocator(2)
    # # ax.xaxis.set_major_locator(x_major_locator)
    # # plt.ylim(1,)
    # plt.show()
    # 训练12个小时预测1个小时的，根据之前12个小时的数据得到现在的数据

# 把预测的画到一个图中
def delCpu2Predict():
    filepath = 'C:/Users/24302/Desktop/毕设安排/项目相关/GraduationProject-Toolcode-Windows/cpu2predict.csv'
    readfd = open(filepath, "r")
    reader = csv.reader(readfd)
    cpu = []
    predcpu = []
    for i in reader:
        cpu.append(round(float(i[0]),10))
        predcpu.append(round(float(i[1]),10))
    X = np.linspace(0,len(cpu),len(cpu))
    plt.figure(1)
    plt.title("CPU_Usage_Predict")
    # plt.subplot(211)
    plt.plot(X, cpu, '--', label='real_cpu_usage')
    plt.legend()
    # plt.subplot(212)
    plt.plot(X, predcpu, '-', label='pred_cpu_usage')
    plt.legend()
    plt.title("LcTask load waves")
    plt.xlabel("realtive_time/300s")
    plt.ylabel("gcu_usage")
    plt.show()
    
# 给一行画图
def drawOne():
    filepath = 'C:/Users/24302/Desktop/毕设安排/项目相关/GraduationProject-Toolcode-Windows/cpu2predict.csv'
    reader = csv.reader(open(filepath,"r") )
    Y = []
    for i in reader:
        Y.append(float(i[0]))
    X = np.arange(len(Y))
    plt.figure(1)
    plt.plot(X, Y, '--', label='real_cpu_usage')
    plt.legend()
    plt.ylim(bottom=0)
    plt.show()
if __name__ == '__main__':
    delCpu2Predict()
    # getData()
    # drawOne()




    



