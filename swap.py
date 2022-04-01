import pyperclip as pc

def main(input):
    mappedData = map(float, input.split(","))
    cor = list(mappedData)
    cor[0], cor[1] = cor[1], cor[0]
    output = ', '.join(map(str, cor))
    pc.copy(output)
    print(output)   

if __name__ == "__main__":
    input = input()
    main(input)