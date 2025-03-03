def process_text(input_file_path, output_file_path):
    """读取输入文件的每一行，用逗号拼接后写入输出文件

    Args:
        input_file_path (str): 输入文件路径
        output_file_path (str): 输出文件路径
    """
    try:
        # 读取输入文件
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            lines = input_file.readlines()
        
        # 处理文本：去除每行的首尾空白字符，并用逗号拼接
        processed_text = ','.join(line.strip() for line in lines)
        
        # 写入输出文件
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(processed_text)
            
        print(f'处理完成！结果已保存到：{output_file_path}')
        
    except FileNotFoundError:
        print(f'错误：找不到输入文件 {input_file_path}')
    except Exception as e:
        print(f'发生错误：{str(e)}')

if __name__ == '__main__':
    # 示例用法
    input_file = 'input.txt'
    output_file = 'output.txt'
    process_text(input_file, output_file)