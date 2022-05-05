import random
import time
class make_lib():
    lib_make_start = time.time()
    global map_codex
    global map_lib
    map_codex = [["a1","a2","a3","a4","a5","a6","a7"],["b1","b2","b3","b4","b5","b6","b7"],
                 ["c1","c2","c3","c4","c5","c6","c7"],["d1","d2","d3","d4","d5","d6","d7"],
                 ["e1","e2","e3","e4","e5","e6","e7"],["f1","f2","f3","f4","f5","f6","f7"],
                 ["g1","g2","g3","g4","g5","g6","g7"]]
    map_lib = {}
    alphabet = ["A","B","C","D","E","F","G"]
    for count_codex in range(len(map_codex)):  #EX: a to b (changing the first alphabet of codex)
        token =[]
        token = [alphabet[count_codex],alphabet[6-count_codex],alphabet[0],alphabet[6]]
        token_c = []
        token_c=token.copy()
        map_lib.update({map_codex[count_codex][0]:token})
        for make_lib in range(1,len(map_codex[count_codex])): # EX:  a1 to a2 (changing the second num of codex)
            token_c[2] = alphabet[alphabet.index(token[2])+1]
            token_c[3] = alphabet[alphabet.index(token[3])-1]
            token = token_c.copy()
            map_lib.update({map_codex[count_codex][make_lib]:token})
            #print(token,token_c)
    print(map_lib)
    lib_make_end = time.time()
    print("Took",lib_make_end - lib_make_start,"sec")
    #print( map_lib[map_codex[0][0]][0] ) #cp


class make_map():
    lenth = int(input("submit lenth"))
    width = int(input("submit width"))
    first_block = random.randint(0,len(map_codex)*len(map_codex[0])-1)
    map_token = []
    map_token.append(map_lib[map_codex[int(first_block/len(map_codex))][first_block%len(map_codex[0])]])
    for first_row in range(width-1):
        comply_token = []
        for fn in range(len(map_codex)):
            for sn in range(len(map_codex[0])):
                if ( ( map_lib[map_codex[fn][sn]] [3] ) == ( map_token[first_row][1] ) )  :
                    comply_token.append(map_lib[map_codex[fn][sn]])
        #print(comply_token)  #cp
        comply_chosen = random.randint(0,len(comply_token)-1)
        map_token.append(comply_token[comply_chosen])
    print("map_token =",map_token)
        
        
    """
    for l in range(1,lenth+1):
        comply_token = []
        print('\n')
        for w in range (width):
            for fn in range(len(map_codex)):
                for sn in range(len(map_codex[0])):
                    if ( (map_lib[map_codex[fn][sn]][3]) == map_token[width+l*width+w-1] [1] ) and ( ( map_lib[map_codex[fn][sn]] [0] ) == ( map_token[l*width+w-1][2] ) ):
                        comply_token.append(map_lib[map_codex[fn][sn]])
        comply_chosen = random.randint(0,len(comply_token)-1)
        map_token.append(comply_token[comply_chosen])
    """
#print( "map_lib = ",map_lib[ map_codex[0][0] ] )  #cp
#map_block = [[]]