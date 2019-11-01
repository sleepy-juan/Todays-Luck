import json

def luck(index, lucktype, messages):
    if lines[index].strip() == lucktype:
        if not len(list(filter(lambda x:x["name"]==lucktype, messages))):
            messages.append({"name":lucktype, "text":[]})
        temp = ""
        index += 1
        while (lines[index].strip() != ""):
            temp += lines[index].strip()
            temp += " "
            index += 1
        list(filter(lambda x:x["name"]==lucktype, messages))[0]["text"].append(temp.strip())
    return index

with open('luckdata.txt', 'r') as f:
    messages = []
    lines = f.readlines()
    index = 0
    while (index < len(lines)):
        index = luck(index, "사업운", messages)
        index = luck(index, "애정운", messages)
        index = luck(index, "건강운", messages)
        index = luck(index, "재물운", messages)
        index += 1

with open('luck.json', 'w') as f:
    json.dump(messages, f)