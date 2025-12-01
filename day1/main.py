
class Data:
    direction:str = ''
    distance:int = 0

    # ctor (constructor)
    def __init__(self, direction:str, distance:int):
        self.direction = direction
        self.distance = distance

    # toString overwrite
    def __str__(self):
        return f"{{{self.direction}, {self.distance}}}"

def extract_data() -> list[Data]:
    result = []
    #with open(r"input") as inp_file:
    with open(r"test_input") as inp_file:
        for l in inp_file:
            result.append(Data(l[0], int(l[1:len(l)-1])))
    return result

    
def solve():
    pass

##
# test input solution is '3' (number of times dial points at 0)
if __name__ == '__main__':
    print(extract_data())