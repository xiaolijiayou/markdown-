import os
import re
import tkinter as tk
from tkinter import filedialog

def replace_image_paths(root_dir, old_folder, new_folder):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    pattern = re.compile(rf'!\[([^\]]*)\]\((.*?){old_folder}(.*?)\)')
                    new_content = pattern.sub(rf'![\1](\2{new_folder}\3)', content)
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                except Exception as e:
                    print(f"处理文件 {file_path} 时出错: {e}")

def select_folder():
    folder = filedialog.askdirectory()
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, folder)

def start_replace():
    root_dir = folder_entry.get()
    old_folder = old_folder_entry.get()
    new_folder = new_folder_entry.get()
    if root_dir and old_folder and new_folder:
        replace_image_paths(root_dir, old_folder, new_folder)
        status_label.config(text="替换完成！")
    else:
        status_label.config(text="请填写所有信息！")

# 创建主窗口
root = tk.Tk()
root.title("Markdown 图片路径替换工具")

# 文件夹选择部分
folder_label = tk.Label(root, text="选择要处理的文件夹:")
folder_label.pack(pady=10)

folder_entry = tk.Entry(root, width=50)
folder_entry.pack(pady=5)

select_button = tk.Button(root, text="选择文件夹", command=select_folder)
select_button.pack(pady=5)

# 旧文件夹名输入部分
old_folder_label = tk.Label(root, text="要更改的文件夹名:")
old_folder_label.pack(pady=10)

old_folder_entry = tk.Entry(root, width=50)
old_folder_entry.pack(pady=5)

# 新文件夹名输入部分
new_folder_label = tk.Label(root, text="重命名后的文件夹名:")
new_folder_label.pack(pady=10)

new_folder_entry = tk.Entry(root, width=50)
new_folder_entry.pack(pady=5)

# 开始替换按钮
start_button = tk.Button(root, text="开始替换", command=start_replace)
start_button.pack(pady=20)

# 状态显示标签
status_label = tk.Label(root, text="")
status_label.pack(pady=10)

# 运行主循环
root.mainloop()