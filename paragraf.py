import sys
import re

class Paragraf:
    setext = re.compile("[=\-]+\s*")
    h1_setext = re.compile("=+\s*")
    h2_setext = re.compile("-+\s*")

    atx = re.compile("#+ .*")
    h1_atx = re.compile("# .*")
    h2_atx = re.compile("## .*")
    h3_atx = re.compile("### .*")
    h4_atx = re.compile("#### .*")
    h5_atx = re.compile("##### .*")
    h6_atx = re.compile("###### .*")

    heading_numbers = [0,0,0,0,0,0]

    def generate_paragraph(self):
        paragraph = "§"

        for number in self.heading_numbers:
            if number is not 0:
                paragraph += str(number)
            else:
                break

        return paragraph + " "

    def run(self):
        with open(sys.argv[1], "r") as f:
            lines = f.readlines()
            print(lines)

            for i, line in (enumerate(lines)):
                if self.h1_setext.match(line):
                    self.heading_numbers[0] += 1
                    lines[i-1] = self.generate_paragraph() + lines[i-1]
                    print(self.heading_numbers)

            #print(lines)
            open("out.md", "w").writelines(lines)

p = Paragraf()
p.run()
