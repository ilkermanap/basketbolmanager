
OK = 1
SG = 2
KF = 3
UF = 4
PV = 5

class Oyuncu:
    def __init__(self, adi, formano, tipi, sut, teknik, savunma, overall):
        self.adi = adi
        self.formano = formano
        self.tip = tipi
        self.sut = sut
        self.teknik = teknik
        self.savunma = savunma
        self.overall = overall
        
class Takim:
    def __init__(self, adi):
        self.adi = adi
        self.ts1 = None  #Top sahibi1
        self.ts2= None  #Top sahibi2
        self.savunma = None
        self.time = None
        self.sertlik = None
        self.hucum = None
        self.players = {}

    def oyuncu_ekle(self, oyuncu):
        self.players[oyuncu.adi] = oyuncu
        

class Mac:
    def __init__(self, home, visitor):
        self.home = home
        self.visitor = visitor

    def play(self):
        #mac burada oynanir
        pass
        
        
class Lig:
    def __init__(self, filename):
        self.filename = filename
        self.teams = {}
        self.name = None
        self.load()
        
    def load(self):
        lines = open(self.filename, "r").readlines()
        tempteam = None
        for line in lines:
            line = line.strip()
            temp = line.split(",")
            if line.startswith("L"):
                self.name = temp[1]
            if line.startswith("T"):
                if tempteam is not None:
                    self.teams[tempteam.adi] = tempteam
                tempteam = Takim(temp[1])
            if line.startswith("O"):
                _, adi, numara, tipi, sut, teknik, savunma, overall = temp
                tempteam.oyuncu_ekle(Oyuncu(adi, int(numara), int(tipi),
                                            float(sut), int(teknik),
                                            int(savunma), int(overall)))
        self.teams[tempteam.adi] = tempteam
