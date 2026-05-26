class TuringMachine:

    def __init__(self, tape):
        self.tape = list(tape) + ["_"] * 30
        self.head = 0
        self.state = "q0"
        self.step = 1

    # Adım gösterimi
    def show_step(self, read, write, move):

        print(f"\nAdım {self.step}")
        print(f"Durum           : {self.state}")
        print(f"Okunan Sembol   : {read}")
        print(f"Yazılan Sembol  : {write}")
        print(f"Kafa Hareketi   : {move}")
        print(f"Bant            : {''.join(self.tape).rstrip('_')}")

        pointer = " " * self.head + "^"
        print(f"                 {pointer}")

        self.step += 1


    def run(self):
# * =
    
        self.state = "q_find_star"

        while self.tape[self.head] != "*":

            current = self.tape[self.head]

            self.show_step(current, current, "R")

            self.head += 1

        self.show_step("*", "*", "R")

        star_index = self.head

      # ayirma işlemi

        birinci = ""
        ikinci = ""

        i = 0

        while self.tape[i] != "*":
            birinci += self.tape[i]
            i += 1

        i = star_index + 1

        while self.tape[i] != "=":
            ikinci += self.tape[i]
            i += 1

        print("\nOperand Ayrıştırma:")
        print("Birinci Sayı  :", birinci)
        print("İkinci Sayı   :", ikinci)


        self.state = "q_multiply"

        result = 0
        shift = 0

        for i in range(len(ikinci) - 1, -1, -1):

            bit = ikinci[i]

            self.show_step(bit, bit, "L")

            if bit == "1":

                print(f"\nBit = 1 -> {birinci} sola kaydırılıyor")

                value = int(birinci, 2) << shift

                result += value

            else:

                print("\nBit = 0 -> toplama yapılmadı")

            shift += 1


        result_binary = bin(result)[2:]

        self.state = "q_write_result"

        while self.tape[self.head] != "=":
            self.head += 1

        self.head += 1

        for bit in result_binary:

            self.show_step("_", bit, "R")

            self.tape[self.head] = bit

            self.head += 1


        self.state = "q_accept"

        print("\n===== SONUÇ =====")
        print("Binary Sonuç :", result_binary)
        print("Decimal      :", result)

#girdi al
sayi1 = input("Birinci binary sayı: ")
sayi2 = input("İkinci binary sayı : ")

binary_mi = True

for ch in sayi1:
    if ch not in ["0", "1"]:
        binary_mi = False

for ch in sayi2:
    if ch not in ["0", "1"]:
        binary_mi = False

if not binary_mi:

    print("HATA: Sadece 0 ve 1 girilebilir.")

else:

    # format
    tape = sayi1 + "*" + sayi2 + "="


#sonuç
    print("\nBaşlangıç Bandı:")
    print(tape)

    tm = TuringMachine(tape)

    tm.run()