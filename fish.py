class Fish:
    def __init__(self, name: str, size: int, speed: int, price: int):
        self.name = name
        self.size = size
        self.speed = speed

    def flee(self) -> None:
        return "The fish escaped."