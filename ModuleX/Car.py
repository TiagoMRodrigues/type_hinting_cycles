MYPY = False
if MYPY:
    import ModuleX.Person as Person


class Car:

    def __init__(self, brand: str, owner: 'Person.Person') -> None:
        self.brand = brand  # type: str
        self.owner = owner  # type: Person.Person

    def get_owner(self) -> 'Person.Person':
        return self.owner
