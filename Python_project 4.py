def concatenate_reverse(str1, str2, str3):
    return str3 + str2 + str1

def main():
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")
    string3 = input("Enter the third string: ")

    result = (string1, string2, string3)
    print(result[::-1])

if __name__ == "__main__":
    main()