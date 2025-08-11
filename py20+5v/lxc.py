# 假设文件是 UTF-8 编码
with open("jm2chonglxc", encoding='utf-8') as f:
    code_map = {}
    for line in f:
        parts = line.strip().split()
        if len(parts) == 2:
            char, code = parts
            code_map[char] = code

with open('lxc.txt', encoding='utf-8') as f:
    for line in f:
        parts = line.strip().split()
        if not parts:
            continue
        head = parts[0]
        words = parts[1:]
        if head in code_map:
            for word in words:
                print(f"{word}\t{code_map[head]}")
