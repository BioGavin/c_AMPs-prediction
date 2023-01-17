import itertools

# 定义天然氨基酸列表
amino_acids = ["A", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "Y"]

# 生成长度为 6 的随机序列
sequences = itertools.product(amino_acids, repeat=5)

# 打开文件
with open("../Jobs/len5seq/sequences.fasta", "w") as f:
    # 遍历序列，并将每个序列写入文件
    for i, sequence in enumerate(sequences):
        # 在每个序列前面添加 ">seq_<i>" 这样的行，以指定序列的 ID
        f.write(">seq_{}\n".format(i))
        # 将序列写入文件，每 80 个字符换一行
        for j in range(0, len(sequence), 80):
            f.write("".join(sequence[j:j + 80]) + "\n")
