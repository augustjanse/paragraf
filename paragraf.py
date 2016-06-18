#!/usr/bin/env python3

import sys
import re

class Paragraf:
    h1_setext = re.compile("={2,}\s*")
    h2_setext = re.compile("-{2,}\s*")
    setext_patterns = [h1_setext, h2_setext]

    h1_atx = re.compile("# .*")
    h2_atx = re.compile("## .*")
    h3_atx = re.compile("### .*")
    h4_atx = re.compile("#### .*")
    h5_atx = re.compile("##### .*")
    h6_atx = re.compile("###### .*")
    atx_patterns = [h1_atx, h2_atx, h3_atx, h4_atx, h5_atx, h6_atx]

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
        with open(sys.argv[1], "r+") as f:
            lines = f.readlines()

            for i, line in enumerate(lines):
                for j, pattern in enumerate(self.setext_patterns):
                    if pattern.match(line):
                        self.set_heading_numbers(j + 1)
                        lines[i - 1] = self.generate_paragraph() + lines[i - 1]

                for j, pattern in enumerate(self.atx_patterns):
                    if pattern.match(line):
                        self.set_heading_numbers(j + 1)
                        lines[i] = re.sub(r"(#+ )",
                                r"\1" + self.generate_paragraph(),
                                lines[i])

            f.seek(0)
            f.writelines(lines)
            f.truncate()

p = Paragraf()
p.run()
