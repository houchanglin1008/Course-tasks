import datetime
class JudjeTime(object):
    def __init__(self):
        self.start = " 3:00"
        self.end = " 3:20"
    def judje(self):
        n_time = datetime.datetime.now()
        start = datetime.datetime.strptime(str(n_time.date())+self.start,'%Y-%m-%d %H:%M')
        end = datetime.datetime.strptime(str(n_time.date())+self.end,'%Y-%m-%d %H:%M')
        if n_time > start and n_time<end:
            return True
        else:
            return False


if __name__=="__main__":
    print(JudjeTime().judje())