'''用来判断各种与牌型相关的役种的函数'''

import Majhong_Class

def get_index(card):
    '''获取一个张牌在标准牌列表中的索引值'''
        # inhand_cards_list = [
        #         0, 0, 0, 0, 0, 0, 0, 0, 0,  # 1-9万 0-8
        #         0, 0, 0, 0, 0, 0, 0, 0, 0,  # 1-9条 9-17
        #         0, 0, 0, 0, 0, 0, 0, 0, 0,  # 1-9筒 18-26
        #         0, 0, 0, 0, 0, 0, 0  # 东南西北白发中 27-33
        #     ]
    match card[0]:
        case 'w':
            return int(card[1])-1
        case 's':
            return int(card[1])+8
        case 'p':
            return int(card[1])+17
        case 'f':
            match card:
                case 'fEast':
                    return 27
                case 'fSouth':
                    return 28
                case 'fWest':
                    return 29
                case 'fNorth':
                    return 30
                case _:
                    print("Something's wrong with the input")
        case 'y':
            match card:
                case 'yBai':
                    return 31
                case 'yFa':
                    return 32
                case 'yZhong':
                    return 33
                case _:
                    print("Something's wrong with the input")
        case _:
            print("Something's wrong with the input")


def is_Duan19(stardand_card_class:Majhong_Class.Majhong_stardand_class) -> bool:
    '''判断是否断幺九
    Args: 标准化后的麻将牌类:Majhong_stardand_class
    return: 返回int型番数值=1  '''

def is_7Duizi(stardand_card_class:Majhong_Class.Majhong_stardand_class) -> bool:
    '''判断是否七对子
    Args: 标准化后的麻将牌类:Majhong_stardand_class
    return: 判断为七对子,返回bool型数值 return T, 反之 return F '''
    if stardand_card_class.isMenqing == False:
        return False
    else:
        all_cards = stardand_card_class.initialize_card_list(stardand_card_class.get_all_cards())
        if all(card_cnt not in {1,3,4} for card_cnt in all_cards) and sum(all_cards) == 14:
            return True
        else:
            return False

def is_13_19(stardand_card_class:Majhong_Class.Majhong_stardand_class)->bool:
    '''函数检查麻将牌的给定手牌是否是普通国士无双型和牌
    Args: 标准化后的麻将牌类:Majhong_stardand_class
    return: 判断为普通国士无双,返回bool型数值 return T, 若不是 return F '''
    if stardand_card_class.isMenqing == False:
        return False
    else:
        # check_list = []
        total = 0
        cards = stardand_card_class.initialize_card_list(stardand_card_class.get_all_cards())
        index_19_cards = [1, 9, 10, 18, 19, 27, 28, 29, 30, 31, 32, 33, 34]
        for i in index_19_cards:
            c = cards[i - 1]
            total += c
            # check_list.append(c)
            if c not in {1, 2}:
                return False            
        if total == 14:
            return True
        else:
            return False

def is_13_19_13M(stardand_card_class)->bool:
    '''函数检查麻将牌的给定手牌是否是国士无双十三面和牌
    Args: 标准化后的麻将牌类:Majhong_stardand_class
    return: 判断为国士无双十三面,返回bool型数值 return T, 若不是 return F '''
    if stardand_card_class.isMenqing == False:
        return False
    else:
        total = 0
        cards = stardand_card_class.initialize_card_list(stardand_card_class.get_all_cards_without_agari())
        index_19_cards = [1, 9, 10, 18, 19, 27, 28, 29, 30, 31, 32, 33, 34]
        for i in index_19_cards:
            c = cards[i - 1]
            total += c
            if c not in {1}:
                return False     
        if total == 13 and get_index(stardand_card_class.agari[0])+1 in index_19_cards:
            return True
        else:
            return False
