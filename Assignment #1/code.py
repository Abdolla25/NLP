import csv
import re

with open('test.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(":") for line in stripped if any(line))
    with open('output.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('Test', 'Value'))
        writer.writerows(lines)

with open('output.csv', 'r') as f:
    my_csv_text = f.read()

new_csv_str = re.sub('\n\n', ';\n', my_csv_text)

new_csv_path = 'final.csv'
with open(new_csv_path, 'w') as f:
    f.write(new_csv_str)