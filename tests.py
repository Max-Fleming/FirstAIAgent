from functions.write_file_content import write_file


def test():

    result = write_file("calculator", "test.txt", "Hello world")
    print(result)

   


if __name__ == "__main__":
    test()
