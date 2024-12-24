import pandas as pd
import numpy as np 
import os
import matplotlib.pyplot as plt

import platform

if platform.system() == "Darwin":
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
elif platform.system() == "Linux":
    plt.rcParams['font.family'] = ['Droid Sans Fallback', 'DejaVu Sans']
else:
    plt.rcParams['font.sans-serif'] = ['SimHei']

# 绘制分月交易金额柱状图，去除在线充值的数据
def draw_monthly_trade_amount(df,result_path,year,username):
    df_month = df[df['meraddr']!='在线充值']

    # 如果缺少某个月份的数据，会导致绘图时缺少某个月份的柱子，所以需要补全
    df_month = df_month.groupby('month')['txamt'].sum()

    # 补全缺少的月份
    for i in range(1,13):
        mon = i
        # 将个位数的月份转化为两位数
        # if i < 10:
        #     mon = '0' + str(i)
        # else:
        #     mon = str(i)
        
        if mon not in df_month.index:
            df_month.loc[mon] = 0
    df_month = df_month.sort_index()

    # 设置颜色按金额变化
    colors = plt.cm.jet(df_month/df_month.max())
    plt.figure(figsize=(12,6))

    df_month.plot(kind='bar',title=f'{year}年校园卡分月交易金额',rot=0,color=colors)
    # 绘制每个月的交易金额
    for a,b in zip(range(len(df_month)),df_month):
        plt.text(a,b+0.5,'%.2f'%b,ha='center',va='bottom',fontsize=8)
    plt.xlabel('月份')
    plt.savefig(result_path + f'{username}_{year}年分月校园卡交易金额.png')
    #plt.show()

# 绘制分地点交易金额柱状图，并去除在线充值的数据
def draw_location_trade_amount(df,result_path,year,username):
    df_addr = df.groupby('meraddr')['txamt'].sum()
    df_addr = df_addr.drop('在线充值')
    df_addr = df_addr.sort_values(ascending=True)
    plt.figure(figsize=(12,len(df_addr)/5))
    # 设置颜色按金额变化
    colors = plt.cm.cool(df_addr/df_addr.max())
    df_addr.plot(kind='barh',title=f'{year}年校园卡分地点交易金额',fontsize=10,rot=0,color=colors)
    # 绘制每个地点的交易金额
    for a,b in zip(range(len(df_addr)),df_addr):
        plt.text(b,a,'%.2f'%b,ha='left',va='center',fontsize=8)
    plt.ylabel('地点')
    plt.savefig(result_path + f'{username}_{year}年分地点校园卡交易金额.png')
    #plt.show()

# 绘制分窗口交易金额横向柱状图
def draw_window_trade_amount(df,result_path,year,username):
    df_window = df.groupby('mername')['txamt'].sum()
    df_window = df_window.sort_values()

    plt.figure(figsize=(12,len(df_window)/5))
    # 设置颜色按金额变化
    colors = plt.cm.spring(df_window/df_window.max())
    df_window.plot(kind='barh',title=f'{year}年校园卡分窗口交易金额',fontsize=8,color=colors)
    # 绘制每个窗口的交易金额
    for a,b in zip(range(len(df_window)),df_window):
        plt.text(b+0.5,a,'%.2f'%b,ha='center',va='bottom',fontsize=10)
    plt.ylabel('窗口')
    plt.savefig(result_path + f'{username}_{year}年分窗口校园卡交易金额.png')
    #plt.show()

# 绘制分时间交易金额柱状图，去除在线充值的数据
def draw_hourly_trade_amount(df,result_path,year,username):
    df_hour = df[df['meraddr']!='在线充值'].groupby('hour')['txamt'].sum()
    df_hour = df_hour.sort_index()
    plt.figure(figsize=(12,6))
    # 设置颜色按数量变化
    colors = plt.cm.jet(df_hour/df_hour.max())
    df_hour.plot(kind='bar',title=f'{year}年校园卡分时间交易金额',rot=0,color=colors)
    # 绘制每个时间的交易金额
    for a,b in zip(range(len(df_hour)),df_hour):
        plt.text(a,b+0.5,'%.2f'%b,ha='center',va='bottom',fontsize=8)
    plt.xlabel('时间/时刻')
    plt.savefig(result_path + f'{username}_{year}年分时间校园卡交易金额.png')
    #plt.show()

# 绘制分时间交易饼图，去除在线充值的数据
def draw_hourly_trade_amount_pie(df,result_path,year,username):
    df_hour = df[df['meraddr']!='在线充值'].groupby('hour')['txamt'].sum()
    # 按金额排序
    df_hour = df_hour.sort_values()
    plt.figure(figsize=(8,8))
    # 设置颜色按金额变化
    colors = plt.cm.jet(np.linspace(0,1,len(df_hour)))
    df_hour.plot(kind='pie',title=f'{year}年校园卡分时间交易金额',autopct='%1.1f%%',colors=colors,fontsize=10)
    plt.ylabel('')
    plt.axis('equal')
    plt.savefig(result_path + f'{username}_{year}年分时间校园卡交易金额饼图.png')
    #plt.show()

# 绘制分地点交易金额饼图，除去在线充值
def draw_location_trade_amount_pie(df,result_path,year,username):
    df_addr = df.groupby('meraddr')['txamt'].sum()
    df_addr = df_addr.drop('在线充值')
    df_addr = df_addr.sort_values(ascending=True)

    plt.figure(figsize=(8,8))
    # 设置颜色按金额变化
    colors = plt.cm.jet(np.linspace(0,1,len(df_addr)))
    df_addr.plot(kind='pie',title=f'{year}年校园卡分地点交易金额',autopct='%.2f%%',colors=colors,fontsize=10)
    plt.ylabel('')
    plt.axis('equal')
    plt.savefig(result_path + f'{username}_{year}年分地点校园卡交易金额饼图.png')
    #plt.show()

#绘制分月分地点交易金额折线图，除去在线充值
def draw_monthly_location_trade_amount(df,result_path,year,username):
    df_month_addr = df[df['meraddr']!='在线充值'].groupby(['month','meraddr'])['txamt'].sum()
    df_month_addr = df_month_addr.unstack()

    # 填充缺失值
    df_month_addr = df_month_addr.fillna(0)

    # 设置颜色变化
    colors = plt.cm.jet(np.linspace(0,1,len(df_month_addr.columns)))
    plt.figure(figsize=(16,6))
    df_month_addr.plot(title=f'{year}年校园卡分月分地点交易金额变化图',rot=0,color=colors)

    plt.xlabel('月份')
    plt.ylabel('金额')

    plt.legend(title='地点')
    #设置图例位置
    plt.legend(loc='center left',bbox_to_anchor=(1,0.5))

    plt.savefig(result_path + f'{username}_{year}年分月分地点校园卡交易金额.png')
    #plt.show()

# 绘制交易地点次数柱状图
def draw_location_trade_count(df,result_path,year,username):
    df_addr_count = df['meraddr'].value_counts()
    df_addr_count = df_addr_count.sort_values(ascending=True)
    plt.figure(figsize=(12,len(df_addr_count)/5))
    # 设置颜色变化
    colors = plt.cm.jet(np.linspace(0,1,len(df_addr_count)))
    df_addr_count.plot(kind='barh',title=f'{year}年校园卡交易地点总次数排行',rot=0,color=colors)
    # 绘制每个地点的交易次数
    for a,b in zip(range(len(df_addr_count)),df_addr_count):
        plt.text(b,a,f'{b}次',ha='left',va='center',fontsize=8)
    # 设置y轴标签
    plt.ylabel('地点')
    plt.savefig(result_path + f'{username}_{year}年校园卡交易地点总次数排行.png')
    #plt.show()

# 绘制交易窗口次数柱状图
def draw_window_trade_count(df,result_path,year,username):
    df_name_count = df['mername'].value_counts()
    df_name_count = df_name_count.sort_values(ascending=True)
    #df_name_count = df_name_count[20:]
    plt.figure(figsize=(12,len(df_name_count)/5))
    # 设置颜色变化
    colors = plt.cm.jet(np.linspace(0,1,len(df_name_count)))
    df_name_count.plot(kind='barh',title=f'{year}年校园卡交易窗口总次数排行',rot=0,color=colors)
    # 绘制每个窗口的交易次数
    for a,b in zip(range(len(df_name_count)),df_name_count):
        plt.text(b,a,f'{b}次',ha='left',va='center',fontsize=8)
    # 设置y轴标签
    plt.ylabel('窗口')
    plt.savefig(result_path + f'{username}_{year}年校园卡交易窗口总次数排行top20.png')
    #plt.show()

def get_meal_data(df):
    # 早餐：筛选出hour在4——9点的数据，排除meraddr为紫荆公寓6号楼、自助打印成绩单、学生卡成本的数据
    df_breakfast = df[(df['hour']==4)|(df['hour']==5)|(df['hour']==6)|(df['hour']==7)|(df['hour']==8)|(df['hour']==9)|(df['hour']=='4')|(df['hour']=='5')|(df['hour']=='6')|(df['hour']=='7')|(df['hour']=='8')|(df['hour']=='9')|(df['hour']=='04')|(df['hour']=='05')|(df['hour']=='06')|(df['hour']=='07')|(df['hour']=='08')|(df['hour']=='09')]
    df_breakfast = df_breakfast[(df_breakfast['meraddr']!='紫荆公寓6号楼')&(df_breakfast['mername']!='自助打印成绩单')&(df_breakfast['mername']!='学生卡成本')]

    # 午饭：筛选出hour在11——13点的数据，排除meraddr为紫荆公寓6号楼、自助打印成绩单、学生卡成本的数据
    df_lunch = df[(df['hour']==10)|(df['hour']==11)|(df['hour']==12)|(df['hour']==13)|(df['hour']=='10')|(df['hour']=='11')|(df['hour']=='12')|(df['hour']=='13')]
    df_lunch = df_lunch[(df_lunch['meraddr']!='紫荆公寓6号楼')&(df_lunch['mername']!='自助打印成绩单')&(df_lunch['mername']!='学生卡成本')]

    # 晚饭：筛选出hour在16——19点的数据，排除meraddr为紫荆公寓6号楼、自助打印成绩单、学生卡成本的数据
    df_dinner = df[(df['hour']==16)|(df['hour']==17)|(df['hour']==18)|(df['hour']==19)|(df['hour']=='16')|(df['hour']=='17')|(df['hour']=='18')|(df['hour']=='19')]
    df_dinner = df_dinner[(df_dinner['meraddr']!='紫荆公寓6号楼')&(df_dinner['mername']!='自助打印成绩单')&(df_dinner['mername']!='学生卡成本')]

    # 宵夜：筛选出hour在20——23点的数据，排除meraddr为紫荆公寓6号楼、自助打印成绩单、学生卡成本的数据
    df_midnight = df[(df['hour']==20)|(df['hour']==21)|(df['hour']==22)|(df['hour']==23)|(df['hour']=='20')|(df['hour']=='21')|(df['hour']=='22')|(df['hour']=='23')]
    df_midnight = df_midnight[(df_midnight['meraddr']!='紫荆公寓6号楼')&(df_midnight['mername']!='自助打印成绩单')&(df_midnight['mername']!='学生卡成本')]

    return df_breakfast,df_lunch,df_dinner,df_midnight

# 绘制早餐、午饭、晚饭、宵夜常去的食堂的次数柱状图，绘制到一张图上，横坐标为早餐、午饭、晚饭、宵夜，食堂数分别取前三
def draw_meal_canteen_count(df,result_path,year,username):
    # 获取早餐、午饭、晚饭、宵夜的数据
    df_breakfast,df_lunch,df_dinner,df_midnight = get_meal_data(df)

    # 获取早餐、午饭、晚饭、宵夜的食堂数据
    df_breakfast_count_a_day = df_breakfast.drop_duplicates(subset=['month','day'])
    df_breakfast_addr = df_breakfast_count_a_day['meraddr'].value_counts()
    df_breakfast_addr = df_breakfast_addr[:3]

    df_lunch_by_day = df_lunch.drop_duplicates(subset=['month','day'])
    df_lunch_addr = df_lunch_by_day['meraddr'].value_counts()
    df_lunch_addr = df_lunch_addr[:3]

    df_dinner_by_day = df_dinner.drop_duplicates(subset=['month','day'])
    df_dinner_addr = df_dinner_by_day['meraddr'].value_counts()
    df_dinner_addr = df_dinner_addr[:3]

    df_midnight_by_day = df_midnight.drop_duplicates(subset=['month','day'])
    df_midnight_addr = df_midnight_by_day['meraddr'].value_counts()
    df_midnight_addr = df_midnight_addr[:3]

    # 绘制早餐、午饭、晚饭、宵夜常去的食堂的次数柱状图
    df_addr_count = pd.concat([df_breakfast_addr,df_lunch_addr,df_dinner_addr,df_midnight_addr],axis=1)
    df_addr_count.columns = ['早餐','午饭','晚饭','宵夜']
    df_addr_count = df_addr_count.fillna(0)
    df_addr_count = df_addr_count.T
    df_addr_count = df_addr_count.fillna(0)

    # 设置颜色变化
    colors = plt.cm.jet(np.linspace(0,1,len(df_addr_count.columns)))
    df_addr_count.plot(kind='bar',title=f'{year}年早餐、午饭、晚饭、宵夜常去的食堂次数排行',rot=0,color=colors)
    
    # 绘制每个食堂的交易次数
    for a in range(len(df_addr_count)):
        for b in range(len(df_addr_count.columns)):
            # 标注数值，避免互相重叠
            # plt.text(a,b+5,int(df_addr_count.iloc[b,a]),ha='center',va='top',fontsize=8)
            #TODO: 为了避免互相重叠，这里的坐标需要调整，请自行调整调整下行0.2和0.13的值
            plt.text(a-(0.2-b*0.13),int(df_addr_count.iloc[a,b]),int(df_addr_count.iloc[a,b]),ha='center',va='bottom',fontsize=8)
    # 设置标签
    plt.legend(title='食堂')
    # 设置x轴标签
    plt.xlabel('食堂')
    plt.savefig(result_path + f'{username}_{year}年校园卡早餐、午饭、晚饭、宵夜常去的食堂次数排行.png')
    #plt.show()

# 绘制早餐、午饭、晚饭、宵夜常去的窗口的次数柱状图，绘制到一张图上，横坐标为早餐、午饭、晚饭、宵夜，窗口数分别取前三
def draw_meal_window_count(df,result_path,year,username):

    # 获取早餐、午饭、晚饭、宵夜的数据
    df_breakfast,df_lunch,df_dinner,df_midnight = get_meal_data(df)

    # 获取早餐、午饭、晚饭、宵夜的窗口数据
    df_breakfast_name = df_breakfast['mername'].value_counts()
    df_breakfast_name = df_breakfast_name[:3]

    df_lunch_name = df_lunch['mername'].value_counts()
    df_lunch_name = df_lunch_name[:3]

    df_dinner_name = df_dinner['mername'].value_counts()
    df_dinner_name = df_dinner_name[:3]

    df_midnight_name = df_midnight['mername'].value_counts()
    df_midnight_name = df_midnight_name[:3]

    # 绘制早餐、午饭、晚饭、宵夜常去的窗口的次数柱状图
    df_name_count = pd.concat([df_breakfast_name,df_lunch_name,df_dinner_name,df_midnight_name],axis=1)
    df_name_count.columns = ['早餐','午饭','晚饭','宵夜']
    df_name_count = df_name_count.fillna(0)
    df_name_count = df_name_count.T
    df_name_count = df_name_count.fillna(0)

    # 设置颜色变化
    colors = plt.cm.jet(np.linspace(0,1,len(df_name_count.columns)))
    df_name_count.plot(kind='bar',title=f'{year}年早餐、午饭、晚饭、宵夜常去的窗口次数排行',rot=0,color=colors)
    
    # 绘制每个窗口的交易次数
    for a in range(len(df_name_count)):
        for b in range(len(df_name_count.columns)):
            # 标注数值，避免互相重叠
            # plt.text(a,b+5,int(df_name_count.iloc[b,a]),ha='center',va='top',fontsize=8)
            #TODO: 为了避免互相重叠，这里的坐标需要调整，请自行调整调整下行0.21和0.07的值
            plt.text(a - (0.21 - b*0.07),int(df_name_count.iloc[a,b]),int(df_name_count.iloc[a,b]),ha='center',va='bottom',fontsize=8)
    # 设置标签
    plt.legend(title='窗口')
    # 设置x轴标签
    plt.xlabel('窗口')
    plt.savefig(result_path + f'{username}_{year}年校园卡早餐、午饭、晚饭、宵夜常去的窗口次数排行.png')
    #plt.show()

# 绘制分地点交易次数饼图，除去在线充值
def draw_location_trade_count_pie(df,result_path,year,username):
    df_addr_count = df['meraddr'].value_counts()
    df_addr_count = df_addr_count.sort_values(ascending=True)
    #df_addr_count = df_addr_count.drop('在线充值')

    plt.figure(figsize=(8,8))
    # 设置颜色变化
    colors = plt.cm.jet(np.linspace(0,1,len(df_addr_count)))
    df_addr_count.plot(kind='pie',title=f'{year}年校园卡交易地点总次数占比',autopct='%1.1f%%',colors=colors,fontsize=10)
    plt.ylabel('')
    plt.axis('equal')
    plt.savefig(result_path + f'{username}_{year}年校园卡交易地点总次数占比.png')
    #plt.show()

if __name__ == '__main__':
    print('请输入年份')
    year = input()


    # 创建结果文件夹
    result_path = f'./results/{year}/'
    if not os.path.exists(result_path):
        os.makedirs(result_path)
        print(f'创建文件夹 {result_path}.') 
    
    # 读取username
    with open('username.txt', 'r') as f:
        username = f.read()
    print('当前用户为：',username)

    print(f"请输入你所涉及的宿舍楼，请保持与原始数据一致(如紫荆公寓6号楼)，\n可查看",result_path + f'data_{year}_{username}.csv','中的meraddr列')
    apt = input()
    apt = str(apt)

    # 读取数据
    df_all = pd.read_csv(result_path + f'data_{year}_{username}.csv')

    # 绘制分月交易金额柱状图，去除在线充值的数据
    draw_monthly_trade_amount(df_all,result_path,year,username)

    # 绘制分地点交易金额柱状图，并去除在线充值的数据
    draw_location_trade_amount(df_all,result_path,year,username)

    # 绘制分窗口交易金额横向柱状图
    draw_window_trade_amount(df_all,result_path,year,username)

    # 绘制分时间交易金额柱状图，去除在线充值的数据
    draw_hourly_trade_amount(df_all,result_path,year,username)

    # 绘制分时间交易饼图，去除在线充值的数据
    draw_hourly_trade_amount_pie(df_all,result_path,year,username)

    # 绘制分地点交易金额饼图，除去在线充值
    draw_location_trade_amount_pie(df_all,result_path,year,username)

    #绘制分月分地点交易金额折线图，除去在线充值
    draw_monthly_location_trade_amount(df_all,result_path,year,username)

    # 去除在线充值的数据
    df = df_all[df_all['meraddr']!='在线充值']

    # 绘制交易地点次数柱状图
    draw_location_trade_count(df,result_path,year,username)

    # 绘制交易窗口次数柱状图
    draw_window_trade_count(df,result_path,year,username)

    # 去除洗澡、游泳、打印、学生卡成本的数据（欢迎补充，因为本人除吃饭外的开销就这些了hhhhh）
    df_meal = df[(df['meraddr'] != apt) & (df['meraddr'] != '自助打印成绩单') & (df['meraddr'] != '学生卡成本') & (df['meraddr'] != '西湖游泳池') & (df['meraddr'] != '陈明游泳馆')]

    # 绘制早餐、午饭、晚饭、宵夜常去的食堂的次数柱状图，绘制到一张图上，横坐标为早餐、午饭、晚饭、宵夜，食堂数分别取前三
    draw_meal_canteen_count(df_meal,result_path,year,username)

    # 绘制早餐、午饭、晚饭、宵夜常去的窗口的次数柱状图，绘制到一张图上，横坐标为早餐、午饭、晚饭、宵夜，窗口数分别取前三
    draw_meal_window_count(df_meal,result_path,year,username)

    # 绘制分地点交易次数饼图，除去在线充值
    draw_location_trade_count_pie(df,result_path,year,username)