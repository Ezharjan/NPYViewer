import argparse
import numpy as np

# 创建命令行参数解析器
parser = argparse.ArgumentParser(description='Read and print numpy array data.')
parser.add_argument('filepath', help='File path of the .npy file')
parser.add_argument('-p', '--print', action='store_true', help='Print data to terminal')
parser.add_argument('output_filepath', nargs='?', default=None, help='Output file path for saving data')

# 解析命令行参数
args = parser.parse_args()

# 读取 .npy 文件
data = np.load(args.filepath)

# 判断是否需要打印内容
if args.print:
    # 打印内容
    print(data)
else:
    # 判断是否提供了输出文件路径
    if args.output_filepath is None:
        print("请选择使用终端查看数据内容（添加-p）或将内容保存到文件中（填写文件存储路径）")
    else:
        # 将内容保存到文件
        with open(args.output_filepath, 'w') as file:
            file.write(str(data))

