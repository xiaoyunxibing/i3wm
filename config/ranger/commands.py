# 这是一个commands.py的例子。 你可以在这里添加你自己的命令。
#
# 请参考 commands_full.py 以了解所有的默认命令和一个完整的
#  文件。 不要把它们都加在这里，否则你可能会得到一个失效的
# 升级游侠时的命令。

# 下面是一个用于演示的简单命令。
# -----------------------------------------------------------------------------

from __future__ import (absolute_import, division, print_function)

# 你可以根据需要导入任何python模块。
import os

# 你总是需要在这里导入ranger.api.commands来获得Command类。
from ranger.api.commands import Command


# 任何属于 "指挥 "的子类都将被整合到游侠中，成为一个
# 命令。 尝试在ranger中输入":my_edit<ENTER>"!
class my_edit(Command):
    # 类的所谓doc-string将在内置的
    # 帮助，可以通过在ranger里面输入"?c "获得。
    """:my_edit <filename>

    A sample command for demonstration purposes that opens a file in an editor.
    """

    # 当你在ranger中运行这个命令时，执行方法会被调用。
    def execute(self):
        # self.arg(1)是函数的第一个（用空格分隔的）参数。
        # 这样，你可以写":my_edit somefilename<ENTER>"。
        if self.arg(1):
            # self.rest(1)包含self.arg(1)和后面的所有内容。
            target_filename = self.rest(1)
        else:
            # self.fm是一个ranger.core.filemanager.FileManager对象，并给出了
            # 你可以接触到游侠的内部结构。
            # self.fm.thisfile是一个ranger.container.file.File对象，是一个
            # 对当前选定文件的引用。
            target_filename = self.fm.thisfile.path

        # 这是一个通用函数，用于在ranger中打印文本。
        self.fm.notify("Let's edit the file " + target_filename + "!")

        # 在fm.notify中使用bad=True允许你打印错误信息。
        if not os.path.exists(target_filename):
            self.fm.notify("The given file does not exist!", bad=True)
            return

        # 这将执行ranger.core.acitons中的一个函数，这个模块有一个
        # 各种子程序可以帮助你构建命令。
        # 请查看源代码，或者运行 "pydoc ranger.core.actions "获取列表。
        self.fm.edit_file(target_filename)

    # 当你按下tab键时，tab方法被调用，并应返回一个
    # 用户将浏览的建议。
    # tabnum对于<TAB>来说是1，对于<S-TAB>来说默认是-1
    def tab(self, tabnum):
        # 这是一个通用的标签完成函数，它通过遍历
        # 当前目录的内容。
        return self._tab_directory_content()

# 添加以下条目以清空垃圾目录  :empty
class empty(Command):
    """:empty

    Empties the trash directory ~/.Trash
    """

    def execute(self):
        self.fm.run("rm -rf /home/myname/.Trash/")