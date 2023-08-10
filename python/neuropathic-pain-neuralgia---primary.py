# Hayley C Gorton, Roger T Webb, Mathew J Carr, Marcos Delpozo-Banos, Ann John, Darren M Ashcroft, 2023.

import sys, csv, re

codes = [{"code":"A531500","system":"readv2"},{"code":"F262100","system":"readv2"},{"code":"F262500","system":"readv2"},{"code":"F321.00","system":"readv2"},{"code":"F356100","system":"readv2"},{"code":"N242000","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('neuropathic-pain-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["neuropathic-pain-neuralgia---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["neuropathic-pain-neuralgia---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["neuropathic-pain-neuralgia---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)