import sys
import saveLocator
import saveEditor

MAX_FUNCTION = 4

print('DD2 save Editor ver 0.1\nauthor: Hyena\nlocating save file')

addr = saveLocator.get_all_setting_file()
if addr is None:
    print('exiting program, press enter to continue 未找到存档，按回车推出程序')
    dummy = input()
    sys.exit()

print("find following info找到如下信息")
print('save address存档地址: ' + addr["TopFolderAddr"])
print('run address循环地址: ' + addr["NewestRun"])
print('press enter to continue按回车继续:')
dummy = input()

while 1:
    print('function select功能选择:')
    print('1.add 999 candles增加999蜡烛')
    print('2.max affinity满好感度')
    print('3.repair stagecoach修复马车')
    print('4.exit program推出程序')
    function = int(input('input corresponding index and press enter输入对应数字并回车'))
    if function > MAX_FUNCTION or function < 1:
        print('incorrect input输入错误')
        print('------start over-------')
    elif function == MAX_FUNCTION:
        print('exiting program退出中')
        sys.exit()
    else:
        saveEditor.Editor(function, addr)




