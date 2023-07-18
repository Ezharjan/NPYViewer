import argparse
import numpy as np
import os

# 创建命令行参数解析器
parser = argparse.ArgumentParser(description='Read and print numpy array data.')
parser.add_argument('dirpath', help='Root directory path')
parser.add_argument('-p', '--print', action='store_true', help='Print data to terminal')
parser.add_argument('output_dirpath', nargs='?', default=None, help='Output directory path for saving data')

# 解析命令行参数
args = parser.parse_args()

# 遍历指定目录下的所有文件
for root, dirs, files in os.walk(args.dirpath):
    for file_name in files:
        if file_name.endswith('.npy'):
            # 构建输入文件路径
            input_filepath = os.path.join(root, file_name)

            # 读取 .npy 文件
            data = np.load(input_filepath)

            # 构建输出文件路径
            output_filepath = os.path.join(args.output_dirpath, root.replace(args.dirpath, ''), file_name[:-4] + '.txt')

            # 判断是否需要打印内容
            if args.print:
                # 打印内容
                print(data)
            else:
                # 判断是否提供了输出目录路径
                if args.output_dirpath is None:
                    print("请选择使用终端查看数据内容（添加-p）或将内容保存到文件中（填写文件存储路径）")
                else:
                    # 创建输出文件目录（如果不存在）
                    os.makedirs(os.path.dirname(output_filepath), exist_ok=True)

                    # 将内容保存到文件
                    with open(output_filepath, 'w') as file:
                        file.write(str(data))

