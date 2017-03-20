import ModuleX

if __name__ == '__main__':
    peter = ModuleX.Person("peter")
    vw = ModuleX.Car("VW PASSAT", peter)
    peter.add_car(vw)
    # peter.add_car("hello") # uncomment to test mypy
