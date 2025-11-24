def day_of_week(day,month,year) :
    if month < 3 :
        month += 12
        year -= 1
    K = year % 100
    J = year // 100

    f = day + (13 * (month + 1)) // 5 + K + (K // 4) + (J // 4) + (5 * J) 
    
    day_index = f % 7

    days = [ " Saturday ", " Sunday ", " Monday ", " Tuesday "," Wensday ", " Thursday ", " Friday "]
    return days[day_index]
day = int(input(" Enter day of month (1-31) :"))
month = int(input(" Enter month (1-12) :" ))
year = int(input( " enter year : "))
print( " day in your enter date is ",day_of_week(day,month,year)) 