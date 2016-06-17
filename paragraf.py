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

        for i in range(0, len(self.heading_numbers)):
            if self.heading_numbers[i] is not 0:
                paragraph += str(self.heading_numbers[i])
            else:
                break

            if self.heading_numbers[i + 1] is not 0:
                paragraph += "."

        return paragraph + " "

    def set_heading_numbers(self, heading):
        self.heading_numbers[heading - 1] += 1 # increment given heading
        for i in range(heading, len(self.heading_numbers)): # reset the following
            self.heading_numbers[i] = 0

    def run(self):
        with open(sys.argv[1], "r") as f:
            lines = f.readlines()
            print(lines)

            for i, line in (enumerate(lines)):
                if self.h1_setext.match(line):
                    self.set_heading_numbers(1)
                    lines[i-1] = self.generate_paragraph() + lines[i-1]
                    print(self.heading_numbers)

                if self.h2_setext.match(line):
                    self.set_heading_numbers(2)
                    lines[i-1] = self.generate_paragraph() + lines[i-1]
                    print(self.heading_numbers)

            #print(lines)
            open("out.md", "w").writelines(lines)

p = Paragraf()
p.run()
