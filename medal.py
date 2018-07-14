
class Medal(object):
    def __init__(self, country, gold, silver, bronze):
        self.country = country
        self.gold = gold
        self.silver = silver
        self.bronze = bronze

    def addmedal(self, ranking):
        if ranking == 1:
            self.gold += 1
        elif ranking == 2:
            self.silver += 1
        elif ranking == 3:
            self.bronze += 1

    @property
    def count(self):
        return self.gold + self.silver + self.bronze

    def __str__(self):
        return "%s : gold %d\tsilver %d\tbronze %d\ttotal %d"\
              % (self.country, self.gold, self.silver, self.bronze, self.count)


def ranking(tables):
    print "******ranking by gold metals******"
    tables.sort(key=lambda x: x.gold, reverse=True)
    for i in tables:
        print i
    print "******ranking by total metals******"
    tables.sort(key=lambda x: x.count, reverse=True)
    for i in tables:
        print i


if __name__ == "__main__":
    China = Medal('China', 5,6,7)
    America = Medal('America',7,4,6)
    UK = Medal('England',4,6,3)
    metal_table = [China, America, UK]
    ranking(metal_table)
    print "China got a gold!"
    China.addmedal(1)
    ranking(metal_table)
