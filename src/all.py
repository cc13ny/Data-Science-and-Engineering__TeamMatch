import random

class Member(object):
    def __init__(self, uid):
        self.uid = uid
        self.score = random.randint(0, 100)

class Platform(object):
    def __init__(self):
        self.members = []
        self.current_uid = 0
    
    def add_memb(self):
        m = self.members
        self.current_uid += 1
        c = self.current_uid
        m.append(Member(c))
    
    def match(self):
        pass
    
''' 
class Member(object):
    def __init__(self, uid, name, email, passport):
        self.uid = uid
        self.name = name
        self.email = email
        self.passort = passport
        self.scores =
    
    def know_achieve_typelist(self):
        pass
    
    def know_my_achievelist(self):
        pass
    
    def claim_achieve(self):
        pass

class Admin(object):
    def __init__(self):
        self.playerlist = []

class Score(object):
    def __init__(self):
        pass
    
class Object(object):
    def __init__(self):
        self.type

'''
  
