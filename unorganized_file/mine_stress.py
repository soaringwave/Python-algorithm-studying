# Lv.2
# 광물 캐기

def solution(picks, minerals):
    # priority que will be good
    # because have to use priority
    # count each mines
    minerals_count = []
    for i in range(0, len(minerals) // 5):
        print(i)
        minerals_tmp = minerals[i*5:i*5+5]
        dia_count = minerals_tmp.count("diamond")
        iron_count = minerals_tmp.count("iron")
        stone_count = minerals_tmp.count("stone")
        minerals_count.append([dia_count, iron_count, stone_count])
    if len(minerals) % 5 != 0:
        minerals_tmp = minerals[-(len(minerals) % 5) : len(minerals)]
        print("last", minerals_tmp)
        dia_count = minerals_tmp.count("diamond")
        iron_count = minerals_tmp.count("iron")
        stone_count = minerals_tmp.count("stone")
        minerals_count.append([dia_count, iron_count, stone_count])
    print(minerals_count)
    minerals_count.sort(key=lambda x: (-x[0], -x[1], -x[2]))
    print(minerals_count)
    answer = 0
    return answer