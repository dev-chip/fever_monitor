"""
GUI logger class using a text-edit widget.
"""

__author__ = "James Cook"
__copyright__ = "Copyright 2021"
__license__ = "GNU General Public License v3.0"
__version__ = "1.0.0"
__maintainer__ = "James Cook"
__email__ = "contact@cookjames.uk"


from logging import Handler, Formatter
from PyQt5 import QtGui


class QPlainTextEditLogger(Handler):
    """
        A logger handler to output color-coded log messages to a Qt textView GUI
    """
    def __init__(self, textView):
        """
            init
        """
        Handler.__init__(self)
        self.widget = textView
        self.setFormatter(Formatter(fmt='[%(asctime)s]  %(levelname)s:  %(message)s',
                                            datefmt='%H:%M:%S'))
        self.palette = QtGui.QPalette()
        self.html = ""

    def emit(self, record):
        """
            Handler recieves a message, output it with an appriate color to
            the textView
        """
        msg = self.format(record)
        if "VERBOSE:" in msg:
            self.html += ('<font color="DodgerBlue">' + msg + '\n</color>')
        elif "DEBUG:" in msg:
            self.html += ('<font color="blue">' + msg + '\n</color>')
        elif "ERROR:" in msg:
            self.html += ('<font color="red">' + msg + '\n</color>')
        elif "WARNING:" in msg:
            self.html += ('<font color="Orange">' + msg + '\n</color>')
        else:
            self.html += ('<font color="black">' + msg + '\n</color>')
        self.widget.setHtml("<pre>" + self.html + "</pre>")
        self.widget.verticalScrollBar().setValue(self.widget.verticalScrollBar().maximum())

    def write(self, m):
        """
            Overrides the inherited method
        """
        pass


if __name__ == "__main__":
    print ("No module test implemented.")
