import os
import json


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

    print('done editing执行完毕')


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

# editProfile('./test_json/profile_1.json')
# editAffinity('./test_json/affinity_manager.json')
editStagecoachStatus('./test_json/run_values.json')


