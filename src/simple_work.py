def main(a, b: str):
    return a + b


if __name__ == '__main__':
    m = main("A\t", "B\n")
    print(m)
