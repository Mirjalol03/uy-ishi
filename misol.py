# def eng_kop_takrorlangan_son(lst:list):
#     if not lst:
#         return -1
#     dic = {}
#     for i in lst:
#         dic[i] = dic.get(i,0)+1
#     return max(lst, key = dic.get)

# lst = [1, 2, 4, 5, 6, 4, 3, 4, 3, 4]
# print(f"Enga kop takrorlangan son: {eng_kop_takrorlangan_son(lst)}")

# -----------------------------------------------------


def filmlar_royxati(cinema:list, n:str):
    nums = []
    for i in cinema:
        if n in i['genre']:
            nums.append(i)
    return nums
    if not nums:
        return []
    
cinema = [
    {"title": "Avatar", "genre": "Fantastika", "price": 40000},
    {"title": "Sherlock", "genre": "Detektiv", "price": 30000},
    {"title": "Oq yo‘l", "genre": "Drama", "price": 25000},
    {"title": "Dune", "genre": "Fantastika", "price": 35000}
]
n = input("Film nomini kirting: ")
print(filmlar_royxati(cinema, n))
