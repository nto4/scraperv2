if __name__ == '__main__':

    # clean duplicates
    with open('result.txt', "r") as d:
        data = d.read().splitlines()


    print(len(data))

    data = set(data)
    data = list(data)

    print(len(data))

    with open("withoutdupresult.txt", "a+") as file_object:
        for m in data:
            file_object.write("\n" + str(m) )
