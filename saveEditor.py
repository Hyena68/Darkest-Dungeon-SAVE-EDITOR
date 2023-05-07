import os
import json

relics = {
        "def": "gold",
        "qty": 40,
        "pQty": 0,
        "duration_amount_remaining": 0,
        "name": "Relics"
    }

baubles = {
        "def": "valley_baubles",
        "qty": 40,
        "pQty": 0,
        "duration_amount_remaining": 0,
        "name": "Rural Riches"
    }

def Editor(function: int, addr: dict):
    if function == 1:   # 999 candles
        path = os.path.join(addr['TopFolderAddr'], addr['ProfileSetting'])
        editProfile(path)
    elif function == 2:   # max affinity
        path = os.path.join(addr['NewestRun'], addr['Affinity'])
        editAffinity(path)
    elif function == 3:   # repair stagecoach
        path = os.path.join(addr['NewestRun'], addr['RunValue'])
        editStagecoachStatus(path)
    elif function == 4:
        path = os.path.join(addr['NewestRun'], addr['RunValue'])
        editUpgradePoint(path)
    elif function == 5:
        path = os.path.join(addr['NewestRun'], addr['Inventory'])
        editInventory(path)

    print('done editing执行完毕')
    print('------------------')


def editProfile(path):
    with open(path, 'r') as file:
        # print('success opening file')
        data = json.load(file)
        file.close()

    data["m_ProfileValues"]["m_Values"][0][1] = 999.0

    with open(path, 'w') as file:
        json.dump(data, file, indent=4)
        file.close()


def editAffinity(path):
    with open(path, 'r') as file:
        # print('success opening file')
        data = json.load(file)
        file.close()

    for relation in data["m_Connections"]:
        relation['m_Leaning'] = 20

    with open(path, 'w') as file:
        json.dump(data, file, indent=4)
        file.close()


def editStagecoachStatus(path):
    with open(path, 'r') as file:
        # print('success opening file')
        data = json.load(file)
        file.close()

    data["values"]["torch"] = 99.0
    data["values"]["stage_coach_armor"] = 3.0
    data["values"]["stage_coach_wheels"] = 3.0

    with open(path, 'w') as file:
        json.dump(data, file, indent=4)
        file.close()


def editUpgradePoint(path):
    with open(path, 'r') as file:
        # print('success opening file')
        data = json.load(file)
        file.close()

    data["values"]["hero_upgrade_points"] += 20.0

    with open(path, 'w') as file:
        json.dump(data, file, indent=4)
        file.close()


def addItem(item: dict, data: dict):
    for i in range(len(data["m_items"])):
        if data["m_items"][i] is None:
            data["m_items"][i] = item
            return
    print('fail to add item to inventory, already full!')


def editInventory(path):
    with open(path, 'r') as file:
        # print('success opening file')
        data = json.load(file)
        file.close()

    addItem(relics, data)
    addItem(baubles, data)

    with open(path, 'w') as file:
        json.dump(data, file, indent=4)
        file.close()


# editProfile('./test_json/profile_1.json')
# editAffinity('./test_json/affinity_manager.json')
# editStagecoachStatus('./test_json/run_values.json')
# editInventory('./test_json/inventory.json')

