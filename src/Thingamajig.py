import typing

class Thingamajig:
    def __init__(self, name: str = "thingamajig", data: dict = {}, methods: dict = {}):
        self.name: str = name
        self.data: dict = data
        self.methods: dict = methods
        self.childs: dict = {}
        self.parent: any = None
        
    def set_parent(self, parent: any):
        assert parent != self.parent, f"{self.name} has same parent as given! ({parent})"
        if type(parent).__name__ == "Thingamajig":
            parent.add_child(self)
        else:
            self.parent = parent
        
    def add_child(self, child: any):
        assert not child in self.childs, f"{self.name} already has {child} child!"
        self.childs[child] = child
        if type(child).__name__ == "Thingamajig":
            child.parent = self
    
    def get_data(self, index: str = "all"):
        if index == "all":
            return self.data
        else:
            assert index in self.data, f"impossible to find {index} data in {self.data} of {self.name}!"
            return self.data[index]
        
    def get_method(self, index: str = "all"):
        if index == "all":
            return self.methods
        else:
            assert index in self.methods, f"impossible to find {index} method in {self.methods} of {self.name}!"
            return self.methods[index]
        
    def execute_method(self, index: str, *arguments: any):
        assert index in self.methods, f"impossible to find {index} method in {self.methods} of {self.name}!"
        self.methods[index](self, arguments)
