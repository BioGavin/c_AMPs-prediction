import os
import re
import gzip


def read_fasta(fasta_file):
    if fasta_file.endswith('.gz'):
        with gzip.open(fasta_file, 'rt') as f:
            data_string = f.read().strip()
    else:
        with open(fasta_file, 'r') as f:
            data_string = f.read().strip()
    seq_dict = {}
    lines = data_string.split('\n')
    for i in range(0, len(lines), 2):
        header = lines[i][1:]
        polymer = lines[i + 1].strip()
        seq_dict[header] = polymer
    return seq_dict


def save_seq(seq_dict, output_dir, chunk_size):
    chunk_num = 0
    seq_list = []
    for k, v in seq_dict.items():
        seq_list.append(f'>{k}\n{v}')
        if len(seq_list) == chunk_size:
            chunk_num += 1
            output_file = os.path.join(output_dir, f'chunk_{chunk_num}.fasta.gz')
            with gzip.open(output_file, 'wt') as f:
                f.write('\n'.join(seq_list))
            seq_list = []
    if seq_list:
        chunk_num += 1
        output_file = os.path.join(output_dir, f'chunk_{chunk_num}.fasta.gz')
        with gzip.open(output_file, 'wt') as f:
            f.write('\n'.join(seq_list))


if __name__ == '__main__':
    input_file = "/Users/zhouzhenyi/Documents/SCIProject/NRPSNetwork/c_AMPs-prediction/Jobs/len6seq/len6seq.fasta.gz"
    output_dir = "/Users/zhouzhenyi/Documents/SCIProject/NRPSNetwork/c_AMPs-prediction/Jobs/len6seq/child_fasta"
    chunk_size = 3200000
    seq_dict = read_fasta(input_file)
    save_seq(seq_dict, output_dir, chunk_size)
