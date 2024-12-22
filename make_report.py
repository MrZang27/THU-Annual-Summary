import pandas as pd
import os

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

    # 读取处理过的有效信息表格
    df_data = pd.read_csv(result_path + f'{username}_{year}年校园卡交易总结记录.csv')


    # 生成Markdown标题
    tilte = f"# 华清大学{year}年校园卡年度总结"

    sub_title_0 = f"## 0.申明\n"
    sub_title_0_content = f"""
> 项目数据获取主体框架来源于[Ze-en Xiong](https://github.com/leverimmy)。

> 项目的 idea 来源于 [Rose-max111](https://github.com/Rose-max111)。

> 项目数据获取方式可见[数据获取](https://github.com/leverimmy/THU-Annual-Eat)。

> 项目的数据分析与展示制作由本人[Zang Lee](https://github.com/MrZang27)完成。
    """

    # 总览
    # 获取数据
    # 在校园卡上的总消费金额与次数
    total_spent = df_data.loc[df_data['事项'] == '总交易金额与次数','金额'].values[0]
    visit_count = df_data.loc[df_data['事项'] == '总交易金额与次数','时间'].values[0]

    # 最常去的食堂
    most_visited_canteen = df_data.loc[df_data['事项'] == '最常去的食堂', '地点'].values[0]
    most_visited_canteen_count = df_data.loc[df_data['事项'] == '最常去的食堂', '时间'].values[0]
    most_visited_canteen_spent = df_data.loc[df_data['事项'] == '最常去的食堂', '金额'].values[0]

    # 最常去的窗口
    most_visited_window = df_data.loc[df_data['事项'] == '最常去的窗口', '地点'].values[0]
    most_visited_window_count = df_data.loc[df_data['事项'] == '最常去的窗口', '时间'].values[0]
    most_visited_window_spent = df_data.loc[df_data['事项'] == '最常去的窗口', '金额'].values[0]

    #累计消费最多的食堂
    most_spent_canteen = df_data.loc[df_data['事项'] == '累计消费最多的食堂', '地点'].values[0]
    most_spent_canteen_count = df_data.loc[df_data['事项'] == '累计消费最多的食堂', '时间'].values[0]
    most_spent_canteen_spent = df_data.loc[df_data['事项'] == '累计消费最多的食堂', '金额'].values[0]

    #累计消费最多的窗口
    most_spent_window = df_data.loc[df_data['事项'] == '累计消费最多的窗口', '地点'].values[0]
    most_spent_window_count = df_data.loc[df_data['事项'] == '累计消费最多的窗口', '时间'].values[0]
    most_spent_window_spent = df_data.loc[df_data['事项'] == '累计消费最多的窗口', '金额'].values[0]

    #单次交易金额最大值
    max_spent_for_one_time = df_data.loc[df_data['事项'] == '单次交易金额最大值', '金额'].values[0]
    max_spent_for_one_time_time = df_data.loc[df_data['事项'] == '单次交易金额最大值', '时间'].values[0]
    max_spent_for_one_time_location = df_data.loc[df_data['事项'] == '单次交易金额最大值', '地点'].values[0]

    #单次交易金额最小值
    min_spent_for_one_time = df_data.loc[df_data['事项'] == '单次交易金额最小值', '金额'].values[0]
    min_spent_for_one_time_time = df_data.loc[df_data['事项'] == '单次交易金额最小值', '时间'].values[0]
    min_spent_for_one_time_location = df_data.loc[df_data['事项'] == '单次交易金额最小值', '地点'].values[0]

    #交易金额平均值
    average_spent = df_data.loc[df_data['事项'] == '交易金额均值', '金额'].values[0]

    #交易金额分月最大值与最小值
    max_spent_month = df_data.loc[df_data['事项'] == '交易金额分月最大值', '时间'].values[0]
    max_spent_month_cost = df_data.loc[df_data['事项'] == '交易金额分月最大值', '金额'].values[0]
    min_spent_month = df_data.loc[df_data['事项'] == '交易金额分月最小值', '时间'].values[0]
    min_spent_month_cost = df_data.loc[df_data['事项'] == '交易金额分月最小值', '金额'].values[0]

    #交易金额分地点最大值与最小值
    max_spent_location = df_data.loc[df_data['事项'] == '交易金额分地点最大值', '地点'].values[0]
    max_spent_location_cost = df_data.loc[df_data['事项'] == '交易金额分地点最大值', '金额'].values[0]
    min_spent_location = df_data.loc[df_data['事项'] == '交易金额分地点最小值', '地点'].values[0]
    min_spent_location_cost = df_data.loc[df_data['事项'] == '交易金额分地点最小值', '金额'].values[0]

    #交易金额分时间最大值与最小值
    max_spent_hour = df_data.loc[df_data['事项'] == '交易金额分时间最大值', '时间'].values[0]
    max_spent_hour_cost = df_data.loc[df_data['事项'] == '交易金额分时间最大值', '金额'].values[0]
    min_spent_hour = df_data.loc[df_data['事项'] == '交易金额分时间最小值', '时间'].values[0]
    min_spent_hour_cost = df_data.loc[df_data['事项'] == '交易金额分时间最小值', '金额'].values[0]

    #分月与天交易金额最大值与最小值
    max_spent_day = df_data.loc[df_data['事项'] == '分月与天交易金额最大值', '时间'].values[0]
    max_spent_day_cost = df_data.loc[df_data['事项'] == '分月与天交易金额最大值', '金额'].values[0]
    min_spent_day = df_data.loc[df_data['事项'] == '分月与天交易金额最小值', '时间'].values[0]
    min_spent_day_cost = df_data.loc[df_data['事项'] == '分月与天交易金额最小值', '金额'].values[0]

    #去过的食堂与窗口
    canteen_count = df_data.loc[df_data['事项'] == '去过的食堂','时间'].values[0]
    canteen_count = canteen_count[6:]
    canteen_count = canteen_count[:-1]
    canteen_count = int(canteen_count)

    canteen_list = df_data.loc[df_data['事项'] == '去过的食堂','地点'].values[0]

    window_count = df_data.loc[df_data['事项'] == '去过的窗口','时间'].values[0]
    window_count = window_count[6:]
    window_count = window_count[:-1]
    window_count = int(window_count)
    

    sub_title_1 = f"## 1.总览\n"
    sub_title_1_content = f"""
{year}年， **{username}** 在华清大学校园卡上共消费 **{total_spent}** 元， **{visit_count}** 交易成功，\n
其中最常去的食堂是 **{most_visited_canteen}** ，共消费 **{most_visited_canteen_spent}** 元， **{most_visited_canteen_count}** 到访；\n
最常去的窗口是 **{most_visited_window}** ，共消费 **{most_visited_window_spent}** 元， **{most_visited_window_count}** 到访。\n
![图片]({result_path}{username}_{year}年校园卡交易地点总次数排行.png) \n
![图片]({result_path}{username}_{year}年校园卡交易窗口总次数排行top20.png) \n

累计消费最多的食堂是 **{most_spent_canteen}** ，共消费 **{most_spent_canteen_spent}** 元；\n
累计消费最多的窗口是 **{most_spent_window}** ，共消费 **{most_spent_window_spent}** 元。\n
![图片]({result_path}{username}_{year}年分地点校园卡交易金额.png) \n
![图片]({result_path}{username}_{year}年分窗口校园卡交易金额.png) \n

在 **{max_spent_for_one_time_time}** 时，你为了 **{max_spent_for_one_time_location}** 进行了{year}年最大的一笔消费，花了 **{max_spent_for_one_time}** 元；\n
在 **{min_spent_for_one_time_time}** 时，你为了 **{min_spent_for_one_time_location}** 进行了{year}年最小的一笔消费，花了 **{min_spent_for_one_time}** 元。\n

你{year}年平均每次刷校园卡花费 **{average_spent}** 元。\n\n

还记得 **{max_spent_month}** 发生了什么吗，你在这个月消费最多，共消费了 **{max_spent_month_cost}** 元；\n
一个月的时间太长，那你还记得 **{max_spent_day}** 发生了什么吗，你在这一天消费最多，共消费了 **{max_spent_day_cost}** 元。\n
另外 **{min_spent_month}** 是不是已经放假回家，你在这个月只消费了 **{min_spent_month_cost}** 元。\n    
同时，你在有消费的日子中 **{min_spent_day}** 消费最少，只花了 **{min_spent_day_cost}** 元。\n
![图片]({result_path}{username}_{year}年分月校园卡交易金额.png) \n

{year}年，你每天最喜欢在 **{max_spent_hour}** 时刷卡，共消费了 **{max_spent_hour_cost}** 元；\n
你在 **{min_spent_hour}** 时刷卡最少，只花了 **{min_spent_hour_cost}** 元。\n
![图片]({result_path}{username}_{year}年分时间校园卡交易金额饼图.png) \n
    
你这一年里一共去过 **{canteen_count}**个食堂，**{window_count}**个窗口。\n
分别这些食堂分别是 **{canteen_list}** \n

"""
    if canteen_count >= 10:
        sub_title_1_content += f"去过如此之多的食堂，堪称华清干饭王！ \n"
    elif canteen_count < 5:
        sub_title_1_content += f"才去了{canteen_count}个食堂，是不是该多尝试一下其他食堂呢？ \n"
    else:
        sub_title_1_content += f"华清之大，等你继续探索！ \n"
    
    # 早餐
    # 获取数据

    # 吃早餐总次数
    breakfast_count = df_data.loc[df_data['事项'] == '吃早餐总次数','时间'].values[0]
    breakfast_count_int = breakfast_count[6:]
    breakfast_count_int = breakfast_count_int[:-1]
    #print(breakfast_count_int)
    breakfast_count_int = int(breakfast_count_int)
    breakfast_spent = df_data.loc[df_data['事项'] == '吃早餐总次数','金额'].values[0]

    # 吃早餐最常去的食堂
    breakfast_most_visited_canteen = df_data.loc[df_data['事项'] == '吃早餐最常去的食堂', '地点'].values[0]
    breakfast_most_visited_canteen_count = df_data.loc[df_data['事项'] == '吃早餐最常去的食堂', '时间'].values[0]
    breakfast_most_visited_canteen_spent = df_data.loc[df_data['事项'] == '吃早餐最常去的食堂', '金额'].values[0]

    # 吃早餐最常去的窗口
    breakfast_most_visited_window = df_data.loc[df_data['事项'] == '吃早餐最常去的窗口', '地点'].values[0]
    breakfast_most_visited_window_count = df_data.loc[df_data['事项'] == '吃早餐最常去的窗口', '时间'].values[0]
    breakfast_most_visited_window_spent = df_data.loc[df_data['事项'] == '吃早餐最常去的窗口', '金额'].values[0]

    # 吃早餐最早时间
    breakfast_earliest_time = df_data.loc[df_data['事项'] == '吃早餐最早时间', '时间'].values[0]
    breakfast_earliest_time_cost = df_data.loc[df_data['事项'] == '吃早餐最早时间', '金额'].values[0]
    breakfast_earliest_time_location = df_data.loc[df_data['事项'] == '吃早餐最早时间', '地点'].values[0]

    # 吃早餐最晚时间
    breakfast_latest_time = df_data.loc[df_data['事项'] == '吃早餐最晚时间', '时间'].values[0]
    breakfast_latest_time_cost = df_data.loc[df_data['事项'] == '吃早餐最晚时间', '金额'].values[0]
    breakfast_latest_time_location = df_data.loc[df_data['事项'] == '吃早餐最晚时间', '地点'].values[0]


    sub_title_2 = f"## 2.早餐\n"

    if breakfast_count_int < 100:
        sub_title_2_content_1 = f"""
{year}年，你在华清大学共吃了 **{breakfast_count_int}** 顿早餐，共花费 **{breakfast_spent}** 元。\n
生活虽忙，也要记得好好吃早餐！\n

"""
        
    else:
        sub_title_2_content_1 = f"""
{year}年，你在华清大学共吃了 **{breakfast_count_int}** 顿早餐，共花费 **{breakfast_spent}** 元。\n
早餐是一天中最重要的一餐，坚持吃早餐，保持不错继续坚持！\n

"""
    sub_title_2_content_2 = f"""
还记得 **{breakfast_earliest_time}** 的时候，你在 **{breakfast_earliest_time_location}** 吃早餐，花了 **{breakfast_earliest_time_cost}** 元，这是你{year}年吃得最早的一餐；\n

当然，也别忘了 **{breakfast_latest_time}** 的时候，你在 **{breakfast_latest_time_location}** 吃早餐，花了 **{breakfast_latest_time_cost}** 元，虽然晚起了一会，但是也坚持去吃了早餐。\n

{year}年，你最喜欢去 **{breakfast_most_visited_canteen}** 吃早餐， **{breakfast_most_visited_canteen_count}** 在这里吃了早餐，共花费了 **{breakfast_most_visited_canteen_spent}** 元；\n
**{breakfast_most_visited_window}** 是你早餐的最爱， **{breakfast_most_visited_window_count}** 在这里点了早餐，共花费了 **{breakfast_most_visited_window_spent}** 元。\n

"""

    # 午饭
    # 获取数据

    # 吃午饭总次数
    lunch_count = df_data.loc[df_data['事项'] == '吃午饭总次数','时间'].values[0]
    lunch_count_int = lunch_count[6:]
    lunch_count_int = lunch_count_int[:-1]
    lunch_count_int = int(lunch_count_int)
    lunch_spent = df_data.loc[df_data['事项'] == '吃午饭总次数','金额'].values[0]

    # 吃午饭最常去的食堂
    lunch_most_visited_canteen = df_data.loc[df_data['事项'] == '吃午饭最常去的食堂', '地点'].values[0]
    lunch_most_visited_canteen_count = df_data.loc[df_data['事项'] == '吃午饭最常去的食堂', '时间'].values[0]
    lunch_most_visited_canteen_spent = df_data.loc[df_data['事项'] == '吃午饭最常去的食堂', '金额'].values[0]

    # 吃午饭最常去的窗口
    lunch_most_visited_window = df_data.loc[df_data['事项'] == '吃午饭最常去的窗口', '地点'].values[0]
    lunch_most_visited_window_count = df_data.loc[df_data['事项'] == '吃午饭最常去的窗口', '时间'].values[0]
    lunch_most_visited_window_spent = df_data.loc[df_data['事项'] == '吃午饭最常去的窗口', '金额'].values[0]

    # 吃午饭最早时间
    lunch_earliest_time = df_data.loc[df_data['事项'] == '吃午饭最早时间', '时间'].values[0]
    lunch_earliest_time_cost = df_data.loc[df_data['事项'] == '吃午饭最早时间', '金额'].values[0]
    lunch_earliest_time_location = df_data.loc[df_data['事项'] == '吃午饭最早时间', '地点'].values[0]

    # 吃午饭最晚时间
    lunch_latest_time = df_data.loc[df_data['事项'] == '吃午饭最晚时间', '时间'].values[0]
    lunch_latest_time_cost = df_data.loc[df_data['事项'] == '吃午饭最晚时间', '金额'].values[0]
    lunch_latest_time_location = df_data.loc[df_data['事项'] == '吃午饭最晚时间', '地点'].values[0]

    sub_title_3 = f"## 3.午饭\n"
    sub_title_3_content = f"""
{year}年，你在华清大学共吃了 **{lunch_count_int}** 顿午饭，共花费 **{lunch_spent}** 元。\n
    
还记得 **{lunch_earliest_time}** 的时候就已经点好了 **{lunch_earliest_time_location}** ，这顿午饭花了 **{lunch_earliest_time_cost}** 元,这是你{year}年午餐吃得最早的一次；\n

另外，在 **{lunch_latest_time}** 的时候才去吃午饭，吃的是 **{lunch_latest_time_location}** ，花了 **{lunch_latest_time_cost}** 元\n

{year}年，你最喜欢去 **{lunch_most_visited_canteen}** 吃午饭， **{lunch_most_visited_canteen_count}** 在这里吃了午饭，共花费了 **{lunch_most_visited_canteen_spent}** 元；\n
**{lunch_most_visited_window}** 是你午餐的最爱， **{lunch_most_visited_window_count}** 在这里点了午餐，共花费了 **{lunch_most_visited_window_spent}** 元。\n
    

"""

    # 晚饭

    # 获取数据

    # 吃晚饭总次数
    dinner_count = df_data.loc[df_data['事项'] == '吃晚饭总次数','时间'].values[0]
    dinner_count_int = dinner_count[6:]
    dinner_count_int = dinner_count_int[:-1]
    dinner_count_int = int(dinner_count_int)
    dinner_spent = df_data.loc[df_data['事项'] == '吃晚饭总次数','金额'].values[0]

    # 吃晚饭最常去的食堂
    dinner_most_visited_canteen = df_data.loc[df_data['事项'] == '吃晚饭最常去的食堂', '地点'].values[0]
    dinner_most_visited_canteen_count = df_data.loc[df_data['事项'] == '吃晚饭最常去的食堂', '时间'].values[0]
    dinner_most_visited_canteen_spent = df_data.loc[df_data['事项'] == '吃晚饭最常去的食堂', '金额'].values[0]

    # 吃晚饭最常去的窗口
    dinner_most_visited_window = df_data.loc[df_data['事项'] == '吃晚饭最常去的窗口', '地点'].values[0]
    dinner_most_visited_window_count = df_data.loc[df_data['事项'] == '吃晚饭最常去的窗口', '时间'].values[0]
    dinner_most_visited_window_spent = df_data.loc[df_data['事项'] == '吃晚饭最常去的窗口', '金额'].values[0]

    # 吃晚饭最早时间
    dinner_earliest_time = df_data.loc[df_data['事项'] == '吃晚饭最早时间', '时间'].values[0]
    dinner_earliest_time_cost = df_data.loc[df_data['事项'] == '吃晚饭最早时间', '金额'].values[0]
    dinner_earliest_time_location = df_data.loc[df_data['事项'] == '吃晚饭最早时间', '地点'].values[0]

    # 吃晚饭最晚时间
    dinner_latest_time = df_data.loc[df_data['事项'] == '吃晚饭最晚时间', '时间'].values[0]
    dinner_latest_time_cost = df_data.loc[df_data['事项'] == '吃晚饭最晚时间', '金额'].values[0]

    dinner_latest_time_location = df_data.loc[df_data['事项'] == '吃晚饭最晚时间', '地点'].values[0]

    sub_title_4 = f"## 4.晚饭\n"

    sub_title_4_content = f"""
{year}年，你在华清大学共吃了 **{dinner_count_int}** 顿晚饭，共花费 **{dinner_spent}** 元。\n

**{dinner_earliest_time}** 就已经去点好了 **{dinner_earliest_time_location}** ，这顿晚饭花了 **{dinner_earliest_time_cost}** 元,这是你{year}年晚餐吃得最早的一次；\n

在 **{dinner_latest_time}** 的时候，已经快到宵夜时间你才去吃晚饭，吃的是 **{dinner_latest_time_location}** ，花了 **{dinner_latest_time_cost}** 元\n

{year}年，你最喜欢去 **{dinner_most_visited_canteen}** 吃晚饭， **{dinner_most_visited_canteen_count}** 在这里吃了晚饭，共花费了 **{dinner_most_visited_canteen_spent}** 元；\n
**{dinner_most_visited_window}** 是你晚餐的最爱， **{dinner_most_visited_window_count}** 在这里点了晚餐，共花费了 **{dinner_most_visited_window_spent}** 元。\n

"""
    
    # 宵夜

    # 获取数据

    # 吃宵夜总次数
    midnight_snack_count = df_data.loc[df_data['事项'] == '吃宵夜总次数','时间'].values[0]
    midnight_snack_count_int = midnight_snack_count[6:]
    midnight_snack_count_int = midnight_snack_count_int[:-1]
    midnight_snack_count_int = int(midnight_snack_count_int)
    midnight_snack_spent = df_data.loc[df_data['事项'] == '吃宵夜总次数','金额'].values[0]

    # 吃宵夜最常去的食堂
    midnight_snack_most_visited_canteen = df_data.loc[df_data['事项'] == '吃宵夜最常去的食堂', '地点'].values[0]
    midnight_snack_most_visited_canteen_count = df_data.loc[df_data['事项'] == '吃宵夜最常去的食堂', '时间'].values[0]
    midnight_snack_most_visited_canteen_spent = df_data.loc[df_data['事项'] == '吃宵夜最常去的食堂', '金额'].values[0]

    # 吃宵夜最常去的窗口
    midnight_snack_most_visited_window = df_data.loc[df_data['事项'] == '吃宵夜最常去的窗口', '地点'].values[0]
    midnight_snack_most_visited_window_count = df_data.loc[df_data['事项'] == '吃宵夜最常去的窗口', '时间'].values[0]
    midnight_snack_most_visited_window_spent = df_data.loc[df_data['事项'] == '吃宵夜最常去的窗口', '金额'].values[0]

    # 吃宵夜最早时间
    midnight_snack_earliest_time = df_data.loc[df_data['事项'] == '吃宵夜最早时间', '时间'].values[0]
    midnight_snack_earliest_time_cost = df_data.loc[df_data['事项'] == '吃宵夜最早时间', '金额'].values[0]
    midnight_snack_earliest_time_location = df_data.loc[df_data['事项'] == '吃宵夜最早时间', '地点'].values[0]

    # 吃宵夜最晚时间
    midnight_snack_latest_time = df_data.loc[df_data['事项'] == '吃宵夜最晚时间', '时间'].values[0]
    midnight_snack_latest_time_cost = df_data.loc[df_data['事项'] == '吃宵夜最晚时间', '金额'].values[0]
    midnight_snack_latest_time_location = df_data.loc[df_data['事项'] == '吃宵夜最晚时间', '地点'].values[0]

    sub_title_5 = f"## 5.宵夜\n"

    sub_title_5_content = f"""
{year}年，你在华清大学共吃了 **{midnight_snack_count_int}** 顿宵夜，共花费 **{midnight_snack_spent}** 元。\n

{year}年，你最早在 **{midnight_snack_earliest_time}** 的时候就去点了 **{midnight_snack_earliest_time_location}** ，这顿宵夜花了 **{midnight_snack_earliest_time_cost}** 元, 这是你{year}年宵夜吃得最早的一次；\n

在 **{midnight_snack_latest_time}** 的时候，已经是深夜了你才去吃宵夜，压着食堂关门的时间，吃上了 **{midnight_snack_latest_time_location}** ，花了 **{midnight_snack_latest_time_cost}** 元\n

{year}年，你最喜欢去 **{midnight_snack_most_visited_canteen}** 吃宵夜， **{midnight_snack_most_visited_canteen_count}** 在这里吃了宵夜，共花费了 **{midnight_snack_most_visited_canteen_spent}** 元；\n
**{midnight_snack_most_visited_window}** 是你宵夜的最爱， **{midnight_snack_most_visited_window_count}** 在这里点了宵夜，共花费了 **{midnight_snack_most_visited_window_spent}** 元。\n

"""
    # 吃饭总览
    sub_title_6 = f"## 6.吃饭总览\n"

    sub_title_6_content = f"""
{year}年，你在华清大学共吃了 **{breakfast_count_int}** 顿早餐，共花费 **{breakfast_spent}** 元；\n
吃了 **{lunch_count_int}** 顿午饭，共花费 **{lunch_spent}** 元；\n
吃了 **{dinner_count_int}** 顿晚饭，共花费 **{dinner_spent}** 元；\n
吃了 **{midnight_snack_count_int}** 顿宵夜，共花费 **{midnight_snack_spent}** 元。\n

一日四餐最爱去的食堂分别是 **{breakfast_most_visited_canteen}** 、 **{lunch_most_visited_canteen}** 、 **{dinner_most_visited_canteen}** 和 **{midnight_snack_most_visited_canteen}** ；\n

![图片]({result_path}{username}_{year}年校园卡早餐、午饭、晚饭、宵夜常去的窗口次数排行.png) \n
![图片]({result_path}{username}_{year}年校园卡早餐、午饭、晚饭、宵夜常去的食堂次数排行.png) \n

"""
    
    # 洗澡
    # 获取数据

    # 洗澡总次数
    bath_count = df_data.loc[df_data['事项'] == '洗澡总次数','时间'].values[0]
    bath_count_int = bath_count[5:]
    bath_count_int = bath_count_int[:-1]
    bath_count_int = int(bath_count_int)
    bath_spent = df_data.loc[df_data['事项'] == '洗澡总次数','金额'].values[0]

    # 洗澡最晚时间
    bath_latest_time = df_data.loc[df_data['事项'] == '洗澡最晚时间', '时间'].values[0]
    bath_latest_time_cost = df_data.loc[df_data['事项'] == '洗澡最晚时间', '金额'].values[0]
    bath_latest_time_location = df_data.loc[df_data['事项'] == '洗澡最晚时间', '地点'].values[0]

    # 最常洗澡时间
    bath_most_time = df_data.loc[df_data['事项'] == '最常洗澡时间', '时间'].values[0]
    bath_most_time_cost = df_data.loc[df_data['事项'] == '最常洗澡时间', '金额'].values[0]
    bath_most_time_location = df_data.loc[df_data['事项'] == '最常洗澡时间', '地点'].values[0]

    sub_title_7 = f"## 7.洗澡\n"

    sub_title_7_content = f"""
{year}年，你在华清大学共洗了 **{bath_count_int}** 次澡，共花费 **{bath_spent}** 元。\n

在 **{bath_latest_time}** 的时候，你才在 **{bath_latest_time_location}** 洗完澡，花费了 **{bath_latest_time_cost}** 元\n

{year}年，你最喜欢在 **{str(bath_most_time[5:])}** 的时候去 **{bath_most_time_location}** 洗澡，在这个时间段里你一共花了 **{bath_most_time_cost}** 元\n

"""
    # 生成Markdown内容
    markdown_content = f"""
{tilte}

{sub_title_0}
{sub_title_0_content}

{sub_title_1}
{sub_title_1_content}

{sub_title_2}
{sub_title_2_content_1}
{sub_title_2_content_2}

{sub_title_3}
{sub_title_3_content}

{sub_title_4}
{sub_title_4_content}

{sub_title_5}
{sub_title_5_content}

{sub_title_6}
{sub_title_6_content}

{sub_title_7}
{sub_title_7_content}

"""
    
    with open(f'{username}_Annual_Summary_{year}.md', 'w', encoding='utf-8') as f:
        f.write(markdown_content)






