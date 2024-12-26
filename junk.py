import sys

N = sys.argv()
try:
    with open("text.txt", "r") as f:
        text_data = f.read()

    list = text_data.split(" ")
    dict = {}
    for x in list:
        if x in dict.keys():
            dict[x] += 1
        elif x != '':
            dict[x] = 1
    sorted_dict = sorted(dict.items(), key=lambda i:i[1], reverse=True)
    for i in range(N):
        print(f"{i+1} word \"{sorted_dict[i][0]}\" {sorted_dict[i][1]} times")
except Exception as e:
    print(f"Error: {e}")