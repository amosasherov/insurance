

class calc_func:
    def __init__(self):
        pass


    ### LIFE ###

    def offspring(self, kids, income):
        smallest = kids[0]["age"]
        for now in kids:
            smallest = min(now["age"], smallest)
        return self.offspring_calc(smallest, income)


    def offspring_calc(self, kid, income):
        return income*12*(21-kid)



    def eldery(self, dependants):
        est_end = 84 ### Will Be Replaced With person.gender in order to get more specific detail
        results = {}
        for person in dependants:
            results[person["id"]] = person["mcost"]*12*(est_end-person["age"])
        return results


    ### HEALTH ###

    
