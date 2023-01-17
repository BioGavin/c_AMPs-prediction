#!/usr/bin/python3

import sys

# Parse command line arguments
import pandas as pd

att_bact_file = sys.argv[1]
lstm_bact_file = sys.argv[2]
bert_bact_file = sys.argv[3]
sequence_file = sys.argv[4]
result_output = sys.argv[5]

# Read in the prediction files and store the results in a hash table
# with the line number as the key and the prediction as the value
results = {}

# Read in att_bact.txt
with open(att_bact_file, 'r') as f:
    for i, line in enumerate(f):
        line = line.strip()
        if float(line) > 0.5:
            results[i] = 1
        else:
            results[i] = 0

# Read in lstm_bact.txt
with open(lstm_bact_file, 'r') as f:
    for i, line in enumerate(f):
        line = line.strip()
        if float(line) > 0.5:
            results[i] += 1
        else:
            results[i] += 0

# Read in bert_bact.txt
with open(bert_bact_file, 'r') as f:
    for i, line in enumerate(f):
        line = line.strip()
        if float(line) > 0.5:
            results[i] += 1
        else:
            results[i] += 0

# Print the number of sequences that were processed
print("There are {} sequences need to predictive.".format(len(results)))
print("name;AMP_prediction(1/0);")

# Read in the sequence file and append the prediction to each sequence
with open(sequence_file, 'r') as f:
    data_ls = f.readlines()
    res_ls = []
    for idx in range(len(data_ls)):
        if data_ls[idx].startswith('>'):
            # print(type(idx))
            header = data_ls[idx].strip()[1:]
            seq = data_ls[idx + 1].strip()
            length = len(seq)
            prediction = results[idx/2]
            if prediction == 3:
                prediction = 1
            else:
                prediction = 0
            res_ls.append({
                "header": header,
                "seq": seq,
                "length": length,
                "prediction": prediction
            })

pd.DataFrame(res_ls).to_csv(result_output, sep='\t', index=False)
