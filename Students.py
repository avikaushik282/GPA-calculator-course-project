import math

class Students1:
    def __init__(self, maths, science, language, drama, music, biology):
        self.maths = maths
        self.science = science
        self.language = language
        self.drama = drama
        self.music = music
        self.biology = biology
    def getGPA(self):
        lis = [(self.maths)*4,(self.science)*5,(self.language)*4,(self.drama)*3,(self.music)*2,(self.biology)*4]
        sum_lis = sum(lis)
        GPA = sum_lis/22
        return GPA