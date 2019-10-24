#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: xiaguliuxiang
# date: 2019-10-24
# 适配机型: Honor 10,屏幕分辨率:2280x1080
# github: https://github.com/xiaguliuxiang/xiaguliuxiang-python-games
# thanks: https://github.com/SoMessThat/Tmall-99

import os
import random
import time

'''
天猫双11合伙人全民开喵铺,自动完成任务领喵币

使用说明:
1.安装并配置python;
2.手机连接电脑,打开开发人员选项,并开启USB调试;
3.打开手机天猫(淘宝),进入全民开喵铺界面(不用打开任务列表),运行此程序.

本项目仅供学习研究使用,请勿用于商业用途!
'''


# 设置临时环境变量,免去配置adb的麻烦
def set_env():
    parent_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    tools = os.path.join(parent_path, 'tools')
    os.environ['PATH'] = tools + ';' + os.getenv('PATH')


# 随机整数[x,y)
def rnd(x, y):
    return int(random.uniform(x, y))


# 当前时间
def cur_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


# 模拟滑动
def swipe():
    x1 = rnd(600, 800)  # 横坐标1
    y1 = rnd(1500, 1600)  # 纵坐标1
    x2 = rnd(500, 600)  # 横坐标2
    y2 = rnd(600, 800)  # 纵坐标2
    os.system('adb shell input swipe {} {} {} {}'.format(x1, y1, x2, y2))  # 模拟从下往上滑动
    os.system('adb shell input swipe {} {} {} {}'.format(x2, y2, x1, y1))  # 模拟从上往下滑动


# 返回
def back():
    os.system('adb shell input keyevent KEYCODE_BACK')


# 浏览
def browse_task(times, x1, x2, y1, y2):
    print('====== 做任务领喵币,升级喵铺赢红包(坐标:x:{}-{};y:{}-{}) ======'.format(x1, x2, y1, y2))
    for i in range(times):
        print('\r{} 浏览任务({}/{})开始执行,请稍等...'.format(cur_time(), i + 1, times), end="")
        # 点击去浏览
        os.system('adb shell input tap {} {}'.format(rnd(x1, x2), rnd(y1, y2)))
        for j in range(3):  # 滑动前等待3秒,避免网络不好,我的网络怎么这么垃圾!!!
            print("\r{} 浏览任务({}/{})执行中,请稍等...".format(cur_time(), i + 1, times), end="")
            time.sleep(1)
        swipe()
        browse_time = 20  # 浏览页面20秒,避免因计时延迟导致浏览时间不足
        for j in range(browse_time):
            print("\r{} 浏览任务({}/{})执行中,请等待 {} 秒".format(cur_time(), i + 1, times, browse_time - j), end="")
            time.sleep(1)
        print('\r{} 浏览任务({}/{})执行完成,喵喵喵赢红包'.format(cur_time(), i + 1, times))
        back()
        time.sleep(1)
    time.sleep(1)
    print('====== 做任务领喵币,任务执行完成啦(坐标:x:{}-{};y:{}-{}) ======'.format(x1, x2, y1, y2))


if __name__ == '__main__':
    print('***** 仅供学习研究使用,请勿用于商业用途 *****')
    set_env()
    # 点击领喵币(坐标:x:860-970;y:1680-1760),弹出领喵币中心
    os.system('adb shell input tap {} {}'.format(rnd(860, 970), rnd(1680, 1760)))
    time.sleep(3)
    # 签到任务,坐标:x:820-955;y:805-870
    os.system('adb shell input tap {} {}'.format(rnd(820, 955), rnd(805, 870)))
    time.sleep(3)
    browse_task(20, 820, 955, 1180, 1245)  # 任务1,执行20次,坐标:x:820-955;y:1180-1245
    browse_task(4, 820, 955, 1365, 1430)  # 任务2,执行4次,坐标:x:820-955;y:1365-1430
    browse_task(1, 820, 955, 1555, 1620)  # 任务3,执行1次,坐标:x:820-955;y:1555-1620
    browse_task(1, 820, 955, 1740, 1810)  # 任务4,执行1次,坐标:x:820-955;y:1740-1810
    browse_task(1, 820, 955, 1925, 1995)  # 任务5,执行1次,坐标:x:820-955;y:1925-1995
    print('***** 仅供学习研究使用,请勿用于商业用途 *****')
    os.system("pause")
