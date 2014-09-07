# basic
def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a+b

# generator
def power(values):
    for x in values:
        print("powering %s" % x)
        yield x
def adder(values):
    for x in values:
        print("adder %s" % x)
        if x % 2 == 0:
            yield x + 3
        else:
            yield x + 2

# generator に値をわたせる。
# sendで渡すと、yieldで受け取れる
# try, except, throw, close など例外を扱うこともできる
def psychologist():
    print("Print tell me your problems")
    while True:
        answer = yield
        try:
            if answer is not None:
                if answer.endswith("?"):
                    print("Don't ask yourself too much questions")
                elif "good" in answer:
                    print("A that's good, go on")
                elif "bad" in answer:
                    print("Don't be so negative")
        except ValueError:
            yield "ValueError throwed"
        finally:
            print("closed!!")

# main
def main():
    fib = fibonacci()
    for x in range(1, 5):
        print(next(fib))

    # Tokenize
    import tokenize
    reader = open(__file__).readline
    tokens = tokenize.generate_tokens(reader)
    for x in range(1, 15):
        print(next(tokens))

    # power, adder
    elements = [1, 4, 7, 9, 12, 19]
    res = adder(power(elements))
    for x in elements:
        print(next(res))

    # generator can get valued by send
    free = psychologist()
    next(free)
    free.send("I feel bad")
    try:
        print(free.throw(ValueError))
    except ValueError:
        pass
    free.close()

if __name__ == "__main__":
    main()
