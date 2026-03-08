import os

# List of file extensions to ignore (non-code files)
IGNORE_EXTENSIONS = {".txt", ".md", ".png", ".jpg", ".jpeg", ".gif", ".pdf", ".csv", ".json"}

def count_lines_of_code(directory):
    total_lines = 0
    for root, _, files in os.walk(directory):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext not in IGNORE_EXTENSIONS:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        lines = f.readlines()
                        total_lines += len([line for line in lines if line.strip() != ""])
                except:
                    pass  # skip binary or unreadable files
    return total_lines

if __name__ == "__main__":
    directory = os.getcwd()  # current directory
    lines_count = count_lines_of_code(directory)
    print(f"Total lines of code in this directory: {lines_count}")