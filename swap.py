import pyperclip as pc

def main(before_coo):
    mappedData = map(float, before_coo.split(","))
    cor = list(mappedData)
    cor[0], cor[1] = cor[1], cor[0]
    output = ','.join(map(str, cor))
    pc.copy(output)
    print('After: ' + output + '\n')

if __name__ == "__main__":
    while True:
        cordinate = input("Before: ")
        main(cordinate)
        continue