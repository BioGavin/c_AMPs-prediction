# 过滤掉序列中含有X以及小写字母的序列
import re


def read_fasta(fasta_file):
    with open(fasta_file, 'r') as f:
        data_ls = f.readlines()
    seq_dict = {}
    for idx in range(len(data_ls)):
        if data_ls[idx].startswith('>'):
            header = data_ls[idx].strip()[1:]
            polymer = data_ls[idx + 1].strip()
            seq_dict[header] = polymer
    return seq_dict


def has_lowercase(s):
    if re.search("[a-z,X]", s):
        return True
    else:
        return False


def rm_x(seq_dict):
    filtered_seq_dict = {}
    for k, v in seq_dict.items():
        if not has_lowercase(v):
            filtered_seq_dict[k] = v
    return filtered_seq_dict


def save_seq(seq_dict, single_mode_seq_file):
    seqtxt = ''
    for k, v in seq_dict.items():
        seqtxt += '>' + k + '\n'
        seqtxt += v + '\n'
    with open(single_mode_seq_file, 'w') as f:
        f.write(seqtxt)


if __name__ == '__main__':
    seq_dict = read_fasta(
        "/Users/zhouzhenyi/Documents/SCIProject/NRPSNetwork/Needle/data/NRPSN/Bioactivity/DBAASP3_AMPs_Clean.fasta")
    filtered_seq_dict = rm_x(seq_dict)
    save_seq(filtered_seq_dict,
             "/Users/zhouzhenyi/Documents/SCIProject/NRPSNetwork/c_AMPs-prediction/Jobs/DBAASP/APD3_AMPs_Clean_LowercaseXfiltered.fasta")
