import Majhong_Class
import Majhong_func

# ip=['s5','s50','s50','w50','w6','w7','yBai']
# op=[]
# ag=['yBai']
# doi=['s9','fSouth']
# angang = ['fWest','s1']

#七对子测试牌
# ip=['s5','s50','p5','p5','w6','w6','yBai','s2','s2','w8','w8','w9','w9']
# op=[]
# ag=['yBai']
# doi=['s9','fSouth']
# angang = []


#国士无双测试牌
ip=['s9','s1','p1','p9','w1','w9','yBai','yFa','yZhong','fEast','fWest','fSouth','fNorth']
op=[]
ag=['p1']
doi=['s9','fSouth']
angang = []

exg = Majhong_Class.identified_result(ip,op,ag,doi,angang)

eg_stardand = Majhong_Class.Majhong_stardand_class(exg)
yi_state = Majhong_Class.Majhong_yi_state()

card_list = eg_stardand.initialize_card_list(eg_stardand.get_all_cards())
# i=0
# while i<len(card_list): # 计算宝牌指示牌指示的所有宝牌并统计宝牌总数
#     print(card_list[i],end=' ')
#     if (i+1) % 9 == 0 and i!=0:
#         print('\n')
#     i = i + 1
print('\n',Majhong_func.is_13_19_13M(eg_stardand))
print('\n',Majhong_func.is_13_19(eg_stardand))


# 统计宝牌情况
# print('红宝牌有',exg.count_red_dora() ,'枚')
# i = 0
# print("宝牌是:",end='')
# while i<len(eg_stardand.dora): # 计算宝牌指示牌指示的所有宝牌并统计宝牌总数
#     print(eg_stardand.dora[i],end=' ')
#     i = i + 1
# print(',手里共有',exg.count_normal_dora(),'张', '全部宝牌合计', exg.count_normal_dora()+ exg.count_red_dora(),'张')
# print('门清状态',exg.isMenqing())