from time import perf_counter_ns

it_count = 0
n = 0


def Select_Number():
    print("")
    sn = int(input("Selecteer het nummer dat je wilt gebruiken:"))
    if sn == 0:
        print("Dit is geen correct nummer")
        print()
        print()
        Select_Number()
    else:
        Calculate(sn)


def Calculate(n):
    global it_count
    it_count = 0

    start = perf_counter_ns()

    while n != 1:
        if n % 2:
            n = n * 3 + 1
            print(n)
            it_count += 1
        else:
            n = n // 2
            print(n)
            it_count += 1

    end = perf_counter_ns()
    print(
        "Het getal heeft"
        + str(n)
        + " gehaald met maar: "
        + str(it_count)
        + " sprongen (Tijd dat dit heeft gekost: "
        + format(end - start)
        + " nanoseconden.)"
    )
    print()
    Select_Number()


Select_Number()
