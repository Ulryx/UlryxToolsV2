import os

# Force this to your actual project directory
PROJECT_ROOT = os.path.abspath("E:/Github-Stuff/NuttFarms")

IGNORED_FOLDERS = {
    'venv', 'node_modules', '__pycache__', '.git', '.idea', '.vscode',
    'build', 'dist', 'npm-debug.log', 'yarn-error.log', '.mypy_cache',
    '.pytest_cache', '.tox', '.coverage', '.DS_Store', '.cache',
    'Sync', 'vshub', 'SettingsV2', 'AppData', 'Temp', 'logs'
}

IGNORED_FILE_EXTENSIONS = {
    '.lock', '.sqlite', '.sqlite3', '.log', '.tmp', '.bak'
}

def should_ignore(path):
    name = os.path.basename(path)
    if name in IGNORED_FOLDERS:
        return True
    if os.path.isfile(path):
        _, ext = os.path.splitext(name)
        if ext in IGNORED_FILE_EXTENSIONS:
            return True
    return False

def print_structure(start_path=PROJECT_ROOT, prefix=''):
    try:
        full_path = os.path.abspath(start_path)
        if not full_path.startswith(PROJECT_ROOT):
            return  # Hard stop if something weird is going on

        items = sorted(os.listdir(start_path))
    except PermissionError:
        return

    for i, item in enumerate(items):
        path = os.path.join(start_path, item)
        if should_ignore(path):
            continue
        is_last = (i == len(items) - 1)
        connector = '└── ' if is_last else '├── '
        print(f"{prefix}{connector}{item}")
        if os.path.isdir(path):
            extension = '    ' if is_last else '│   '
            print_structure(path, prefix + extension)

if __name__ == '__main__':
    print_structure()
