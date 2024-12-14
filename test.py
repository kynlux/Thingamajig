from src.Thingamajig import Thingamajig

def print_own_name(self, *arguments):
    print(f"{arguments[0][0]}, {self.name}, {arguments[0][1]}")

test_thingamajig1 = Thingamajig("test_thingamajig1", {"foo": 10}, {"bar": print_own_name})
test_thingamajig2 = Thingamajig("test_thingamajig2")

test_thingamajig1.get_data("foo")