# use to locate the save file

import getpass
import os


def find_profile_folder(TopFolderAddr, target_filename):
    for foldername, subfolders, filenames in os.walk(TopFolderAddr):
        for subfolder in subfolders:
            b_folder_path = os.path.join(foldername, subfolder)
            if is_profile_folder(b_folder_path, target_filename):
                return b_folder_path
    return None


def is_profile_folder(folder_path, target_filename):
    return os.path.exists(os.path.join(folder_path, target_filename))


def get_profiles_folder():
    username = getpass.getuser()
    TopFolderAddr = os.path.join(r'C:\Users', username, r'AppData\LocalLow\RedHook\Darkest Dungeon II\SaveFiles')
    # print(TopFolderAddr)
    target_filename = 'profiles'
    result = find_profile_folder(TopFolderAddr, target_filename)

    if result:
        return result + '\profiles'
    else:
        return None


def get_newest_dir(path):
    newest_file = None
    newest_file_ctime = float('-inf')  # set initial value to negative inf

    with os.scandir(path) as entries:
        for entry in entries:
            # print(entry)
            if entry.is_dir():
                file_ctime = entry.stat().st_ctime
                if file_ctime > newest_file_ctime:
                    newest_file = entry.name
                    newest_file_ctime = file_ctime

    return newest_file


def find_dir(path):
    runfile = []
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_dir():
                runfile.append(entry.name)
    return runfile


def get_all_setting_file():
    """
        return a dictionary contains path to target .json file
    """
    addr = {
            'Affinity': 'affinity_manager.json',
            'Inventory': 'inventory.json',
            'RunValue': 'run_values.json',
            'StageCoach': 'stagecoach.json'
        }

    TopFolderAddr = get_profiles_folder()

    if TopFolderAddr is None:
        print('fail to locate')
        return None

    addr.update({"TopFolderAddr": TopFolderAddr, 'ProfileSetting': 'profile_1.json'})

    runfile = find_dir(os.path.join(TopFolderAddr, 'profile_1_runs'))
    addr.update({"RunFile": runfile[0]})

    newestrun = os.path.join(TopFolderAddr, 'profile_1_runs', runfile[0],
                             get_newest_dir(os.path.join(TopFolderAddr, 'profile_1_runs', runfile[0])))
    addr.update({'NewestRun': newestrun})

    return addr


def initalizeManually(path):
    addr = {
        'Affinity': 'affinity_manager.json',
        'Inventory': 'inventory.json',
        'RunValue': 'run_values.json',
        'StageCoach': 'stagecoach.json'
    }
    addr.update({"TopFolderAddr": path, 'ProfileSetting': 'profile_1.json'})

    runfile = find_dir(os.path.join(path, 'profile_1_runs'))
    addr.update({"RunFile": runfile[0]})

    newestrun = os.path.join(path, 'profile_1_runs', runfile[0],
                             get_newest_dir(os.path.join(path, 'profile_1_runs', runfile[0])))
    addr.update({'NewestRun': newestrun})

    return addr



# print(get_profiles_folder())
# print(get_all_setting_file())
# print(initalizeManually(r'C:\Users\lenovo\AppData\LocalLow\RedHook\Darkest Dungeon II\SaveFiles\a2b87b9734af4f8983298cc3ecda7005\profiles'))




