''' 从视觉识别方法传递回来的牌分为四部分，手牌，副露牌，和牌，宝牌指示牌 
    构建这样一个识别结果类'identified_result'，规范数据信息的传递
    万字牌1~9万,记为w1,w2...w9,其中红5万记为w50;
    饼子牌1~9饼,记为p1,p2...p9,其中红5饼记为p50;
    索子牌1~9索,记为s1,s2...s9,其中红5索记为s50;
    风牌东南西北,记为fEast,fSouth,fWest,fNorth;
    三元牌白,发,中,记为yBai,yFa,yZhong
'''
class identified_result:

    def __init__(self,inhand,outhand,agari,dora_indicator,angang):
        self.inhand = inhand # 手牌
        self.outhand = outhand  # 副露牌
        self.agari = agari  # 和了牌
        self.dora_indicator = dora_indicator # 宝牌指示牌
        self.angang = angang # 暗杠牌,只用一张牌作为指示

    def isMenqing(self):
        '''检查门清状态'''
        if len(self.outhand) == 0:
            return True
        else:
            return False
        
    def define_dora(self,dora_indicator):
        '''根据输入的宝牌指示牌,返回宝牌的值'''
        wangzipai = ['w1','w2','w3','w4','w5','w6','w7','w8','w9']
        suozipai = ['s1','s2','s3','s4','s5','s6','s7','s8','s9']
        bingzipai = ['p1','p2','p3','p4','p5','p6','p7','p8','p9']
        fengpai = ['fEast','fSouth','fWest','fNorth']
        yipai = ['yBai','yFa','yZhong']
        match dora_indicator[0]: #判断宝牌指示牌的类型
            case 'w':
                dora_type = wangzipai
            case 's':
                dora_type = suozipai
            case 'p':
                dora_type = bingzipai
            case 'f':
                dora_type = fengpai
            case 'y':
                dora_type = yipai
            case _:
                print("Something's wrong with the input")
                return 0
        
        if dora_type.index(dora_indicator) < len(dora_type)-1:
            dora_result = dora_type[dora_type.index(dora_indicator) + 1]
        else:
            dora_result = dora_type[0]
        
        return dora_result
    
    def get_normal_dora_list(self): # 根据宝牌指示牌返回宝牌的list
        i = 0
        dora_list = []
        while i<len(self.dora_indicator): # 计算宝牌指示牌指示的所有宝牌
            dora_list.append(self.define_dora(self.dora_indicator[i]))
            i = i + 1
        return dora_list 

    def count_red_dora(self):
        merge_result = self.agari + self.inhand + self.outhand + self.angang + self.angang + self.angang + self.angang
        num_of_red_dora = merge_result.count('w50') + merge_result.count('p50') + merge_result.count('s50') #计算红宝牌个数
        # print("红宝牌一共有:",num_of_red_dora,"枚")
        return num_of_red_dora        
       
    def count_normal_dora(self): # 根据宝牌指示牌计算所有宝牌,统计一共有多少枚
        merge_result = self.agari + self.inhand + self.outhand + self.angang + self.angang + self.angang + self.angang
        if  self.count_red_dora() != 0: #把红宝牌变为普通牌
            merge_result = ['w5' if x == 'w50' else x for x in merge_result]
            merge_result = ['s5' if x == 's50' else x for x in merge_result]
            merge_result = ['p5' if x == 'p50' else x for x in merge_result]
        i = 0
        num_of_dora = 0
        while i<len(self.dora_indicator): # 计算宝牌指示牌指示的所有宝牌并统计宝牌总数
            dora_result = self.define_dora(self.dora_indicator[i])
            # print("宝牌是:",dora_result,end=',')
            num_of_dora = num_of_dora + merge_result.count(dora_result)
            i = i + 1
        return num_of_dora

# 这个类设计了和牌时的各种计算参数,并将和牌时的数据进行标准化,方便计算
class Majhong_stardand_class:
    def __init__(self,results_from_yolo):   
        # 手牌的内容列表
        self.inhand = results_from_yolo.inhand
        # 副录牌的内容列表
        self.outhand = results_from_yolo.outhand
        # 和牌的牌
        self.agari = results_from_yolo.agari
        # 暗杠牌,只用一张牌作为指示
        self.angang = results_from_yolo.angang 
        # 宝牌列表
        self.dora = results_from_yolo.get_normal_dora_list()
        # 红宝牌数量
        self.sum_red_dora = results_from_yolo.count_red_dora()
        # 宝牌数量
        self.sum_normal_dora = results_from_yolo.count_normal_dora()
        # 是否门清
        self.isMenqing = results_from_yolo.isMenqing()
    
    def get_all_cards(self):
        '''返回一个list, 包含暗杠和副露牌在内的所有牌'''
        return self.inhand + self.outhand + self.agari + self.angang + self.angang + self.angang+ self.angang
    
    def get_all_cards_without_agari(self):
        '''返回一个list, 包含除和了牌在内的手牌,暗杠和副露牌在内的所有牌'''
        return self.inhand + self.outhand + self.angang + self.angang + self.angang+ self.angang
    
    def get_inhand_cards(self):
        '''返回一个list, 包含除去暗杠和副露牌之外的所有牌'''
        return self.inhand + self.agari

    def initialize_card_list(self,cards_list):
        '''将手牌标准化'''
        inhand_cards_list = [
            0, 0, 0, 0, 0, 0, 0, 0, 0,  # 1-9万 0-8
            0, 0, 0, 0, 0, 0, 0, 0, 0,  # 1-9条 9-17
            0, 0, 0, 0, 0, 0, 0, 0, 0,  # 1-9筒 18-26
            0, 0, 0, 0, 0, 0, 0  # 东南西北白发中 27-33
        ]
        i = 0
        while i < len(cards_list):
            match cards_list[i][0]:
                case 'w':
                    inhand_cards_list[int(cards_list[i][1])-1] += 1
                case 's':
                    inhand_cards_list[int(cards_list[i][1])+8] += 1
                case 'p':
                    inhand_cards_list[int(cards_list[i][1])+17] += 1
                case 'f':
                    match cards_list[i]:
                        case 'fEast':
                            inhand_cards_list[27] += 1
                        case 'fSouth':
                            inhand_cards_list[28] += 1
                        case 'fWest':
                            inhand_cards_list[29] += 1
                        case 'fNorth':
                            inhand_cards_list[30] += 1
                        case _:
                            print("Something's wrong with the input")
                case 'y':
                    match cards_list[i]:
                        case 'yBai':
                            inhand_cards_list[31] += 1
                        case 'yFa':
                            inhand_cards_list[32] += 1
                        case 'yZhong':
                            inhand_cards_list[33] += 1
                        case _:
                            print("Something's wrong with the input")
                case _:
                    print("Something's wrong with the input")
            i = i + 1
        return inhand_cards_list

            
        
        

class Majhong_yi_state: # 与和牌时状态相关的役种,由用户自行输入
    # 下面是和牌型无关的役种默认值
    def __init__(self):
        # 是否立直
        self.is_Lizhi = False
        # 是否一发
        self.is_Yifa = False

        self.is_Tianhe = False
        self.is_Dihe = False
        self.is_WLizhi = False
        self.is_Hedi = False
        self.is_Haidi = False
        # 是否岭上开花
        self.is_Lingshang = False
        # 是否抢杠
        self.is_Qianggang = False
        # 和牌的方式：自摸，荣和
        self.is_Zimo = False
        # 荣和玩家的方位,从下家开始逆时针数,分别为1,2,3
        self.Dianpao_player = 1
    
    def set_is_Lizhi(self,state):
        self.is_Lizhi = state
    
    def set_is_Yifa(self,state):
        self.is_Yifa = state

    def set_is_Tianhe(self,state):
        self.is_Tianhe = state
    
    def set_is_Dihe(self,state):
        self.is_Dihe = state

    def set_is_WLizhi(self,state):
        self.is_WLizhi = state
    
    def set_is_Hedi(self,state):
        self.is_Hedi = state

    def set_is_Haidi(self,state):
        self.is_Haidi = state
    
    def set_is_Lingshang(self,state):
        self.is_Lingshang = state

    def set_is_Qianggang(self,state):
        self.is_Qianggang = state
    
    def set_is_is_Zimo(self,state):
        self.is_is_Zimo = state
        
    def set_Diaopao_Player(self,position):
        self.Dianpao_player = position
