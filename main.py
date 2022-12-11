import re

alph="abccba cbab cbabcab cabcba bcabac bcabacbabc bacbcabcab acbabacb bcabcacbac bcacbab acbbbacccbac"

def main():
    alph_splited=alph.split()

    for word in alph_splited:
        match = re.search(r'b[a-c]a',word)
        if match:
            print(word)


if __name__ == '__main__':
    main()

# 6. Слова в алфавите {a, b, c}, содержащие подслово вида bxa, где x – произвольная буква алфавита.