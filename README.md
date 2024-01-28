# c_AMPs-prediction
Prediction of new c_AMPs, from the prediction of sORF to the getting c_AMPs. [Scripts](https://github.com/mayuefine/c_AMPs-prediction/blob/master/c_AMPs-Prediction.md "c_AMPs-Prediction.md").<br>
Trained predictive model.[Models](https://github.com/mayuefine/c_AMPs-prediction/tree/master/Models).<br>
Test set data under 50AA in length, and also the benchmark dataset.[Dataset](https://github.com/mayuefine/c_AMPs-prediction/tree/master/Data).<br>
<br>
Verified AMPs have been deposited and published in [ADP database](https://aps.unmc.edu/).<br>
For sequences that have been predicted but not yet verified, please contact **Jun Wang**(junwang\@im.ac.cn) and request a **Material Transfer Agreement (MTA)** to ensure proper usage.<br>

## Installation bert_sklearn
Download and copy [bert_sklearn](https://github.com/mayuefine/c_AMPs-prediction/tree/master/bert_sklearn) to your python3 site-packages folder.<br>
```bash
cd bert-sklearn
pip install .
```
**Please cite**: [Identification of antimicrobial peptides from the human gut microbiome using deep learning](https://www.nature.com/articles/s41587-022-01226-0)



# WLab-Workflow

- 下载资源

```bash
git clone https://github.com/BioGavin/c_AMPs-prediction.git
cd c_AMPs-prediction/
```

- 下载 Bert 模型

从该链接下载 Bert 模型：https://www.dropbox.com/sh/o58xdznyi6ulyc6/AABLckEnxP54j2X7BrGybhyea?dl=0

下载的文件 `bert.bin` 放至 `Models` 路径下

校验模型的完整性

```bash
cd Models
md5sum -c md5.txt
```

输出如下结果表示校验通过，否则说明模型文件下载不完整

```
lstm.h5: OK
att.h5: OK
bert.bin: OK
```

```bash
cd ..  # 返回项目根目录
```

- 创建环境

```bash
conda create -y -n amp_prediction python=3.7 certifi=2022.12.7
conda activate amp_prediction

pip install -r requirement.txt

cd bert_sklearn
pip install .
cd .. && cp -r bert_sklearn/ ~/miniconda3/envs/amp_prediction/lib/python3.7/site-packages/
```

如上述操作成功完成后，下面仍有包报错问题，参考测试时导出的包列表 `requirement_wlabworkflow_reference.txt` 进行手动调试

- 序列格式化

```bash
# 如果有长度超过300的序列，用如下代码删除
seqkit seq -M 300 -g input.faa > output.faa
# 如果fasta文件中的序列是分行的，会导致格式化出现问题，用如下代码将序列转换成一行
seqkit seq -w 0 input.faa > output.faa

# 格式化
cd Data
perl ../script/format.pl len5seq.fasta none > len5seq.txt
```

- Attention 模型预测

```bash
python3 ../script/prediction_attention.py len5seq.txt len5seq.att.txt
```

- LSTM 模型预测

```bash
python3 ../script/prediction_lstm.py len5seq.txt len5seq.lstm.txt
```

- Bert 模型预测

```bash
python3 ../script/prediction_bert.py len5seq.fasta len5seq.bert.txt
```

- 整合结果

```bash
python3 ../script/result.py len5seq.att.txt len5seq.lstm.txt len5seq.bert.txt len5seq.fasta len5seq.result.tsv
```

- 结果可视化

```bash
pip install matplotlib
python3 ../customized_scripts/scatterplot3D.py len5seq.att.txt len5seq.lstm.txt len5seq.bert.txt fig.svg
```

