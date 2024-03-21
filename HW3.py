def fizzbuzz(num1, num2, num3):
    result = ""
    for i in range(1, num3 + 1):
        if i % num1 == 0 and i % num2 == 0:
            result += "FizzBuzz "
        elif i % num1 == 0:
            result += "Fizz "
        elif i % num2 == 0:
            result += "Buzz "
        else:
            result += str(i) + " "
    return result.strip()

with open("test.txt", "r") as file:
    for _ in range(20):
        line = file.readline()
        if not line:
            break

        nums = line.strip().split()
        nums = [int(num) for num in nums]

        for i in range(1, nums[2] + 1):
            result = ""
            if i % nums[0] == 0:
                result += "Fizz"
            if i % nums[1] == 0:
                result += "Buzz"
            if not result:
                result = str(i)
            print(result, end=" ")
        print()
