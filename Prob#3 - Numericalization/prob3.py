def printDigitalNum(numStr, magX, magY):
    # Dict for digital number template (Key is a tuple of (numberDigitStr, row))
    template = {
        ("0", 0): "00000",
        ("0", 1): "0   0",
        ("0", 2): "0   0",
        ("0", 3): "0   0",
        ("0", 4): "00000",

        ("1", 0): "    1",
        ("1", 1): "    1",
        ("1", 2): "    1",
        ("1", 3): "    1",
        ("1", 4): "    1",

        ("2", 0): "22222",
        ("2", 1): "    2",
        ("2", 2): "22222",
        ("2", 3): "2    ",
        ("2", 4): "22222",

        ("3", 0): "33333",
        ("3", 1): "    3",
        ("3", 2): "33333",
        ("3", 3): "    3",
        ("3", 4): "33333",

        ("4", 0): "4   4",
        ("4", 1): "4   4",
        ("4", 2): "44444",
        ("4", 3): "    4",
        ("4", 4): "    4",

        ("5", 0): "55555",
        ("5", 1): "5    ",
        ("5", 2): "55555",
        ("5", 3): "    5",
        ("5", 4): "55555",

        ("6", 0): "66666",
        ("6", 1): "6    ",
        ("6", 2): "66666",
        ("6", 3): "6   6",
        ("6", 4): "66666",

        ("7", 0): "77777",
        ("7", 1): "    7",
        ("7", 2): "    7",
        ("7", 3): "    7",
        ("7", 4): "    7",

        ("8", 0): "88888",
        ("8", 1): "8   8",
        ("8", 2): "88888",
        ("8", 3): "8   8",
        ("8", 4): "88888",

        ("9", 0): "99999",
        ("9", 1): "9   9",
        ("9", 2): "99999",
        ("9", 3): "    9",
        ("9", 4): "99999"
    }

    for i in range(5):
        out = list()
        for c in numStr:
            out.append("".join([ch * magX for ch in template[(c, i)]]))
        out_str = " ".join(out)
        # assumption: the answer does not need to check for terminal width overflow
        for j in range(magY):
            print(out_str)

# assumption: input N is not 0-lead number or a '0' or negative number (from the documentation, specifying positive integer)
N, M1, M2 = [int(i) for i in input().split()]
printDigitalNum(str(N), M1, M2)