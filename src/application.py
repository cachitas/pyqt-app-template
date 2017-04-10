import argparse
import logging
import sys

from PyQt5.QtWidgets import QApplication

from .widgets import ConnectDialog
from .widgets import MainWindow

from . import resources

NAME = 'FlyTracker Condor'
VERSION = '1.0'
ICON = 'fruitfly.ico'

logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--hostname',
        help="Condor hostname to use",
        default='condor.champalimaud.pt',
        type=str,
    )
    parser.add_argument(
        '--username',
        help="Condor username to use",
        default='',
        type=str,
    )
    parser.add_argument(
        '--usergroup',
        help="Condor usergroup to use",
        default='vasconcelos',
        type=str,
    )
    parser.add_argument(
        '--debug',
        help="Print lots of debugging statements",
        action="store_const", dest="log_level", const=logging.DEBUG,
        default=logging.INFO,
    )
    args = parser.parse_args()

    logging.basicConfig(level=args.log_level)

    app = QApplication(sys.argv)
    dialog = ConnectDialog()
    dialog.ui.lineEdit_hostname.setText(args.hostname)
    dialog.ui.lineEdit_username.setText(args.username)
    dialog.ui.lineEdit_usergroup.setText(args.usergroup)
    if dialog.exec():
        main_window = MainWindow()
        main_window.show()
        sys.exit(app.exec())


if __name__ == '__main__':
    main()
