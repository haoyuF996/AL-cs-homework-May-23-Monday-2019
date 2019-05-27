
def sum_polygon( number_of_sides, lenth_of_side ):
    '''
    This function return the sum of the area
    and square of the perimeter of the regular polygon.
    '''
    n = number_of_sides
    s = lenth_of_side
    from math import tan
    from math import pi
    area = (0.5*n*(s**2))/tan(pi/n)
    return round(area,4)
print('Complete program experience polysum')
print(sum_polygon(17,3))


def balance_count_r(balance,annualInterestRate,monthlyPaymentRate,x):
    '''
    This fuction return the balance remain after x months
    '''
    b = balance
    air = annualInterestRate
    mpr = monthlyPaymentRate
    mir = air/12
    if x == 0:
        return b
    else:
        pb = balance_count_r(b,air,mpr,x-1)
        mmp = Minimum_monthly_payment = pb*mpr
        result = (pb-mmp) + mir*(pb-mmp)
        print('Month ',x,' Remaining balance: ',round(result,2))
    return round(result,2)
print('Problem1')
print(balance_count_r(42,0.2,0.04,12))


def balance_count_p(balance,annualInterestRate,monthlyPayment,x):
    '''
    This fuction return the balance remain after x months
    '''
    b = balance
    air = annualInterestRate
    mp = monthlyPayment
    mir = air/12
    if x == 0:
        return b
    else:
        pb = balance_count_p(b,air,mp,x-1)
        result = (pb-mp) + mir*(pb-mp)
    return round(result,2)
    

def lowest_monthly_payment(balance,annualInterestRate,x):
    b = balance
    air = annualInterestRate
    mir = air/12
    l = low = b/x
    h = high = (b+b*(1+mir)**x)/12
    g = guess = (h+l)/2
    o = 0.01
    while abs(balance_count_p(b,air,g,x))>o :
        if balance_count_p(b,air,g,x)>0:
            l = g
        else:
            h = g
        g = guess = (h+l)/2
    return(round(g,2))
print('Problem2')
print('Lowest Payment: $',int(round(lowest_monthly_payment(3926,0.2,12),-1)))
print('Problem3')
print('Lowest Payment: $',lowest_monthly_payment(320000,0.2,12))




        

