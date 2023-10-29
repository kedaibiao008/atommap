import os

# 指定文件名和文本内容
filename = os.path.expanduser("~/atomicals/atomicals-js/4448.atommap.svg")  # 包含完整路径的文件名
svg_content = """
<svg width="200" height="50" xmlns="http://www.w3.org/2000/svg">
    <rect width="100%" height="100%" fill="#ffffff"/>
    <text x="50%" y="50%" font-family="Arial" font-size="20" fill="black" dominant-baseline="middle" text-anchor="middle">4448.atommap</text>
</svg>
"""

# 将文本内容写入文件
with open(filename, "w") as file:
    file.write(svg_content)

print(f"文件 '{filename}' 已成功创建！")
