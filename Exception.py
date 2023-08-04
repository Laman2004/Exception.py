try:
    a=10
    b=0
    if b==0:
        raise Exception
    c=a/b
    d=x
    e="Baku"
    print(e[6])
except ZeroDivisionError:
    print("0-a bolmek olmaz!")
except NameError:
    print("Bele bir deyer yoxdur!")
except IndexError:
    print("Daxil edilen index true deyil!")
except Exception:
    print("Sehviniz var!")
else:
    print("Sehviniz yoxdur:)")
finally:
    print("Hem sehviniz ola,hem de olmaya biler.")
