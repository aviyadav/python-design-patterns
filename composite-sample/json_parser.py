from abc import ABC, abstractmethod


class JSONComponent(ABC):
    """The Component interface sets the common method for all components in the JSON parser."""

    @abstractmethod
    def parse(self):
        """The parse method needs to be implemented by Leaf and Composite classes."""
        pass


class JSONLeaf(JSONComponent):
    """Leaf represents individual elements in the JSON structure."""

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def parse(self):
        """Parsing method for Leaf."""
        return f"Parsing JSON Leaf: {self.key}: {self.value}"


class JSONObject(JSONComponent):
    """Object represents JSON objects that can contain other JSON elements."""

    def __init__(self):
        self.children = []

    def add(self, component):
        """Method to add elements to the JSON Object."""
        self.children.append(component)

    def remove(self, component):
        """Method to remove elements from the JSON Object."""
        self.children.remove(component)

    def parse(self):
        """Parsing method for JSON Object."""
        result = []
        for child in self.children:
            result.append(child.parse())

        return "\n".join(result)


import json

def parse_json(json_string):
    # Parse JSON string
    data = json.loads(json_string)

    # Create root JSON Object
    root = JSONObject()

    # Create nodes based on JSON structure
    for key, value in data.items():
        if isinstance(value, dict):
            obj = JSONObject()
            for k, v in value.items():
                leaf = JSONLeaf(k, v)
                obj.add(leaf)
            root.add(obj)
        else:
            leaf = JSONLeaf(key, value)
            root.add(leaf)

    return root


if __name__ == '__main__':
    # Sample JSON string
    sample_json = '{"name": "John Doe", "age": 30, "address": {"city": "New York", "zip": 10001}}'
    sample_json2 = '{"ptcurmeds":{"code":5,"fieldType":"select"},"psource":{"code":1,"fieldType":"select"},"meanstrans":{"code":2,"fieldType":"select"},"cmo":{"code":2,"fieldType":"select"},"gender":{"code":1,"fieldType":"select"},"smokinghist":{"code":1,"fieldType":"select"},"repcand":{"code":2,"fieldType":"select"},"dschstat":{"code":4,"fieldType":"select"},"stemi":{"code":2,"fieldType":"select"},"cabg":{"code":2,"fieldType":"select"},"nperfpci":{"code":3,"fieldType":"select"},"primarypci":{"code":2,"fieldType":"select"},"hffmc":{"code":2,"fieldType":"select"},"posbio24":{"code":1,"fieldType":"select"},"firstecgdt":{"precision":"minute","fieldType":"date","content":"2018-04-27T10:51:00.00"},"zip":{"fieldType":"text","content":20854},"cardshockfmc":{"code":2,"fieldType":"select"},"transed":{"code":2,"fieldType":"select"},"disdate":{"precision":"day","fieldType":"date","content":"2018-04-30T00:00:00.00"},"race":{"code":6,"fieldType":"select"},"asp24h":{"code":1,"fieldType":"select"},"firstecgobt":{"code":1,"fieldType":"select"},"thromb":{"code":2,"fieldType":"select"},"capriorarr":{"code":2,"fieldType":"select"},"hisethni":{"code":2,"fieldType":"select"},"lvfobtain":{"code":1,"fieldType":"select"},"pateval":{"code":1,"fieldType":"select"},"nadmlytc":{"code":17,"fieldType":"select"},"emsfirst":{"precision":"minute","fieldType":"date","content":"2018-04-27T10:47:00.00"},"noreprsn":{"code":1,"fieldType":"select"},"hxpad":{"code":2,"fieldType":"select"},"ldl":{"fieldType":"integer","content":62},"dob":{"precision":"day","fieldType":"date","content":"1936-01-28T00:00:00.00"},"edtrans":{"precision":"minute","fieldType":"date","content":"2018-04-27T17:05:00.00"},"cardiag":{"code":4,"fieldType":"select"},"admdt":{"precision":"day","fieldType":"date","content":"2018-04-27T00:00:00.00"},"nonemsfirst":{"precision":"unknown","fieldType":"date"},"lvfasmt":{"fieldType":"integer","content":55},"arrdt":{"precision":"minute","fieldType":"date","content":"2018-04-27T11:17:00.00"},"onsetdt":{"precision":"minute","fieldType":"date","content":"2018-04-27T10:30:00.00"}}'

    # Parsing JSON string and creating nodes
    json_structure = parse_json(sample_json2)

    # Displaying the structure and executing parsing
    print(json_structure.parse())