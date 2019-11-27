# -*- coding: UTF-8 -*-
import sys
import os
import subprocess
from conf import settings

app_name = 'travis-pyside2-demo'


def update_windows():
    """将ui文件转换为py文件"""
    _dir_ui = os.path.join(settings.BASE_DIR, 'ui')
    _dir_windows = os.path.join(settings.BASE_DIR, 'windows/ui')
    for file in os.listdir(_dir_ui):
        if file.endswith('.ui'):
            os.system('pyside2-uic -o {} {}'.format(
                os.path.join(_dir_windows, file).rstrip('.ui') + '.py',
                os.path.join(_dir_ui, file)
            ))


def main(extra_args=None):
    update_windows()
    args = [
        'pyinstaller',
        '--specpath', os.path.join(settings.BASE_DIR,
                                   'spec/' + sys.platform),
        '--distpath', os.path.join(settings.BASE_DIR,
                                   'dist/' + sys.platform),
        '--workpath', os.path.join(settings.BASE_DIR, 'build/' + sys.platform),
        '-n', app_name,
        '--hidden-import', 'PySide2.QtPrintSupport',
        '--additional-hooks-dir', 'hooks'
    ]

    if sys.platform == 'darwin':
        args.extend(['-w'])
    elif sys.platform == 'linux':
        args.extend(['-F'])
    else:
        args.extend(['-w'])
    args.extend(['main.py'])
    print(args)
    subprocess.run(args)


if __name__ == "__main__":
    try:
        worker_type = sys.argv[1]
    except IndexError:
        worker_type = 'build'
    if worker_type == 'update_windows':
        update_windows()
        sys.exit(1)
    main()