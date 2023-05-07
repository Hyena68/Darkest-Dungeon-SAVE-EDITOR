import sys
import saveLocator
import saveEditor

MAX_FUNCTION = 5

print('DD2 save Editor ver 0.1\nauthor: Hyena\nlocating save file')
print('please choose scan mode请选择扫描模式:')
print('1.scan automatically自动扫描')
print('2.manually enter address手动输入地址')
scan_mode = int(input('mode模式:'))
if scan_mode == 1:
    addr = saveLocator.get_all_setting_file()
    if addr is None:
        print('exiting program, please input save address manually 未找到存档，请手动输入地址')
        manualAddr = input('address地址: ')
        addr = saveLocator.initalizeManually(str(manualAddr))
elif scan_mode == 2:
    print('please input save address manually 请手动输入地址')
    manualAddr = input('address地址: ')
    try:
        addr = saveLocator.initalizeManually(str(manualAddr))
    except:
        print('fail to locate save file under this address, exiting system无法在该地址下找到存档，退出中')
        dummy = input()
        sys.exit()
else:
    print('incorrect input输入错误')
    print('exiting system退出程序中')
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
    print('4.add 20 upgrade point增加20技能点')
    print('5.add 40 relics and baubles增加40钱和遗产')
    # print('6.unlock all bosses')
    print('0.exit program退出程序')
    function = int(input('input corresponding index and press enter输入对应数字并回车'))
    if function > MAX_FUNCTION or function < 0:
        print('incorrect input输入错误')
        print('------start over-------')
    elif function == 0:
        print('exiting program退出中')
        sys.exit()
    else:
        saveEditor.Editor(function, addr)




