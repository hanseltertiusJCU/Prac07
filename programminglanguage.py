class ProgrammingLanguage:
    def __init__(self,name,typing,status,year=0):
        self.name = name
        self.typing = typing
        self.status = status
        self.year = year

    def is_dynamic(self):
        if self.typing == 'Dynamic':
            return True
        elif self.typing == 'Static':
            return False

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name,self.typing,self.status,self.year)
