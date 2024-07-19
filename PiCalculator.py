import decimal
import time


class Chudnovsky:
    @staticmethod
    def chudnovsky(n):
        try:
            n = int(n)
        except (ValueError, TypeError):
            raise ValueError("n needs to be an integer")

        decimal.getcontext().prec = n * 2 + 15
        C = 426880 * decimal.Decimal(10005).sqrt()
        K = decimal.Decimal(13591409)
        M, X = decimal.Decimal(1), decimal.Decimal(1)
        L = decimal.Decimal(545140134)
        S = K

        for i in range(1, n):
            M = (M * (12 * i - 11) * (12 * i - 7) * (12 * i - 5) * (12 * i - 1)) / (i ** 3 * 640320 ** 3)
            K += L
            X *= -262537412640768000
            S += decimal.Decimal(M * K) / X

        pi = C / S
        return pi

    Choice = input("Find last Pi calculation, or make one! Type C to create a Pi calculation. Or F to find the last one! >")

    Choice_Upper = Choice.upper()

    if Choice_Upper == "C":
        try:
            Input = int(input("Digits to calculate >"))
            n = Input
        except (ValueError, TypeError):
            raise ValueError("n needs to be int")

        if n >= "9999999999999999999":
            raise OverflowError("Too big. Max size is 1,000,000,000,000,000,000.")
            exit(3)
        elif n < "999999999999999999":
            pass

        start_time = time.time()
        calculated_pi = chudnovsky(n)
        end_time = time.time()
        final_time = start_time - end_time
        print(f"Pi to {n} decimal place(s): {str(calculated_pi)[:n + 1]}")
        print(f"Calculation time: {final_time} seconds.")
        print("Thanks to user24714692 for help on Stack Overflow! Using the Chudnovsky formula!")
        str_pi = str(calculated_pi)
        len_str_pi = len(str_pi)
        print("Lenth:", len_str_pi / 2 - 16 + 8)
        File_Open = open("Last_Pi_Calculation", 'w')
        Argument = str(calculated_pi) + "::    Time:    " + str(final_time) + "::    Lenth:    " + str(
            len_str_pi / 2 - 16 + 8)
        File_Write = File_Open.write(Argument)
        File_Open.close()
        exit(2)

    elif Choice_Upper == "F":
        File_Open = open("Last_Pi_Calculation", 'r+')
        File_Read = File_Open.read()
        print(File_Read)
        File_Open.close()
        exit(2)

    else:
        raise TypeError("input must be C or F")
