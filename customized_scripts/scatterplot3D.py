# Usage: python3 scatterplot3D.py att.txt lstm.txt bert.txt output.svg

import sys
import matplotlib.pyplot as plt


att_file, lstm_file, bert_file, output_fig = sys.argv[1:5]

# 1.0 初始化数据
# f(x,y,z) = v
# 其中x,y,z为随机数，v=x*y*z
with open(att_file, 'r') as f:
    x = f.read().splitlines()

with open(lstm_file, 'r') as f:
    y = f.read().splitlines()

with open(bert_file, 'r') as f:
    z = f.read().splitlines()
    
x = [float(i) for i in x]
y = [float(i) for i in y]
z = [float(i) for i in z]

v = [x[i] * y[i] * z[i] for i in range(len(x))]
# 1.1 根据各个点的值(v[])，设置点的颜色值，每个点的颜色使用一个rgb三维的元组表示，例如，若想让点显示为红色，则颜色值为(1.0,0,0)
# 设置各个点的颜色
# 每个点的颜色值按照colormap("seismic",100)进行设计，其中colormap类型为"seismic"，共分为100个级别(level)
min_v = 0
max_v = 1
color = [plt.get_cmap("seismic", 100)(int(float(i - min_v) / (max_v - min_v) * 100)) for i in v]

# 2.0 显示三维散点图
# 新建一个figure()
fig = plt.figure()
# 在figure()中增加一个subplot，并且返回axes
ax = fig.add_subplot(111, projection='3d')
# 设置colormap，与上面提到的类似，使用"seismic"类型的colormap，共100个级别
plt.set_cmap(plt.get_cmap("seismic", 100))
# 绘制三维散点，各个点颜色使用color列表中的值，形状为"."
im = ax.scatter(x, y, z, s=30, c=color, marker='.')
# im = ax.scatter(x, y, z, s=100,c=color,marker='.')
# 2.1 增加侧边colorbar
# 设置侧边colorbar，colorbar上显示的值使用lambda方程设置
position = fig.add_axes([0.9, 0.15, 0.025, 0.6])  # 位置[左,下,宽度,高度]
fig.colorbar(im, cax=position)
# fig.colorbar(im, format=matplotlib.ticker.FuncFormatter(lambda x,pos:int(x*(1-0)+0)))
# 2.2 增加坐标轴标签
ax.set_xlabel('attention')
ax.set_ylabel('lstm')
ax.set_zlabel('bert')
# 2.3显示
plt.savefig(output_fig)
