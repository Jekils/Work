def is_year_leap (years) :
    if (years % 4) == 0 :
        return True
    else :
        return False

print ("Enter years")
years = int(input ())
print (is_year_leap(years))
