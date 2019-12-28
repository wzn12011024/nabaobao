# !/usr/bin/python
# -*-coding:utf8-*-
class Role(object):
    def __init__(self,name,attack):
        self.name = name
        self.rattack = attack
        self.rblood = 100
    def __str__(self):
        pinfo = '角色名：'+self.name+'\n'
        pinfo += '攻击力：'+str(self.rattack)+'\n'
        pinfo += '血量：' +str(self.rblood)
        return pinfo
    def attack(self,r,dead,deadBlood,ro):
        if self.rblood > 0:
            x_blood = r.rblood
            r.rblood -= self.rattack
            if r.rblood >=0:
                if r.rblood == 0:
                    print(dead)
                elif r.rblood < x_blood:
                    print(deadBlood+str(r.rblood))
        else:
            print(ro)
class Person(Role):
   pass
class Dog(Role):
    def __init__(self,name,attack):
        super().__init__(name,attack)
        self.dblood = 100
p = Person('灭霸',5)
print(p)
g = Dog('旺财',10)
print(g)
for i in range(20):
    g.attack(p, '人已死了', '人的剩余血量', '狗已经死亡，不能攻击')
p.attack(g,'狗死了','狗的剩余血量','人已经死亡，不能攻击')
