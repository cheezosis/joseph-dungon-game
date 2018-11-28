
def is_valid(x, y):
    if y>=0 and x == 'single'or x=='married filing jointly' or x=='married filing separately' or x=='widow(er)'or x=='head of household':
         return "True"
    else:
        return "False"
              
def get_tax(x,y):
    if x == 'single':
        if y>=418401:
            return int(932.5 + 4293.75 + 13487.5 + 27930 + 74266.5 + 595 + (y-418400)*.396)
        elif y>=416701:
            return int(932.5 + 4293.75 + 13487.5 + 27930 + 74266.5 + (y-416700)*.35)
        elif y>=191651:
            return int(932.5 + 4293.75 + 13487.5 + 27930 + (y-191650)*.33)
        elif y>=91901:
            return int(932.5 + 4293.75 + 13487.5 + (y-91900)*.28)
        elif y>=37951:
            return int(932.5 + 4293.75 + (y-37950)*.25)
        elif y>=9326:
            return int(932.5 + (y-9325)*.15)
        else:
            return int(y*.10)
        
    elif x=='married filing jointly' or x=='widow(er)':
        if y>=470701:
            return int(1865 + 8587.5 + 19300 + 22470 + 60505.5 + 18900 + (y-470700)*.396)
        elif y>=416701:
            return int(1865 + 8587.5 + 19300 + 22470 + 60505.5 + (y-416700)*.35)
        elif y>=233351:
            return int(1865 + 8587.5 + 19300 + 22470 + (y-233350)*.33)
        elif y>=153101:
            return int(1865 + 8587.5 + 19300 + (y-153100)*.28)
        elif y>=75901:
            return int(1865 + 8587.5 + (y-75900)*.25)
        elif y>=18651:
            return int(1865 + (y-18650)*.15)
        else:
            return int(y*.10)
        
    elif x == 'married filing separately':
        if y>=235351:
            return int(932.5 + 4293.75 + 9650 + 11235 + 30252.75 + 9450 + (y-235350)*.396)
        elif y>=208351:
            return int(932.5 + 4293.75 + 9650 + 11235 + 30252.75 + (y-208350)*.35)
        elif y>=116676:
            return int(932.5 + 4293.75 + 9650 + 11235 + (y-116675)*.33)
        elif y>=76551:
            return int(932.5 + 4293.75 + 9650 + (y-76550)*.28)
        elif y>=37951:
            return int(932.5 + 4293.75 + (y-37950)*.25)
        elif y>=9326:
            return int(932.5 + (y-9325)*.15)
        else:
            return int(y*.10)
        
    elif x == 'head of household':
        if y>=444501:
            return int(1335 + 5617.5 + 20100 + 22764 + 67386 + 9730 + (y-444500)*.396)
        elif y>=416701:
            return int(1335 + 5617.5 + 20100 + 22764 + 67386 + (y-416700)*.35)
        elif y>=212501:
            return int(1335 + 5617.5 + 20100 + 22764 + (y-212500)*.33)
        elif y>=131201:
            return int(1335 + 5617.5 + 20100 + (y-131200)*.28)
        elif y>=50801:
            return int(1335 + 5617.5 + (y-50800)*.25)
        elif y>=13351:
            return int(1335 + (y-13350)*.15)
        else:
            return int(y*.10)
    else:
        return 'Something went wrong'
    
def percent_of_income(x, y):
    return (x/y)*100

def main():
    status = input("Enter status: ")
    income = input("Enter income: ")
    if is_valid(status, int(income)) == "True":
        print("Tax: $ " + str(int(get_tax(status,int(income)))))
        print("Percent of income: " + str(percent_of_income(int(get_tax(status,int(income))),int(income)))+ " %")
    else:
        print('Error')
    