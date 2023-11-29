from my_moduls.generator import Generator


def main():
    generator = Generator()
    value = input("Введите фразу, которую хотите перефразировать:\n")
    print(f"Фраза: {value}")

    generator.rephrase_and_vocalize(value)


if __name__ == '__main__':
    main()