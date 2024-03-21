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

with open("test.txt", "r") as input_file, open("output.txt", "w") as output_file:
    for _ in range(20):
        line = input_file.readline()
        if not line:
            break
        nums = [int(num) for num in line.strip().split()]
        output_file.write(fizzbuzz(*nums) + "\n")