import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                           QHBoxLayout, QLineEdit, QPushButton, QToolBar)
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtGui import QIcon, QPalette, QColor

class ExiledBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Exiled Browser')
        self.setStyleSheet("""
            QMainWindow, QWidget {
                background-color: #1a1a1a;
                color: #ffffff;
            }
            QLineEdit {
                background-color: #2d2d2d;
                border: 1px solid #3d3d3d;
                border-radius: 4px;
                color: #ffffff;
                padding: 5px;
                font-size: 14px;
            }
            QPushButton {
                background-color: #3d3d3d;
                border: none;
                border-radius: 4px;
                color: #ffffff;
                padding: 5px 10px;
                margin: 2px;
            }
            QPushButton:hover {
                background-color: #4d4d4d;
            }
            QToolBar {
                background-color: #2d2d2d;
                border: none;
                spacing: 5px;
                padding: 5px;
            }
        """)

        # Create the main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout(self.central_widget)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        # Create navigation toolbar
        nav_toolbar = QToolBar()
        layout.addWidget(nav_toolbar)

        # Add navigation buttons
        self.back_btn = QPushButton('←')
        self.back_btn.clicked.connect(self.navigate_back)
        nav_toolbar.addWidget(self.back_btn)

        self.forward_btn = QPushButton('→')
        self.forward_btn.clicked.connect(self.navigate_forward)
        nav_toolbar.addWidget(self.forward_btn)

        self.reload_btn = QPushButton('↻')
        self.reload_btn.clicked.connect(self.reload_page)
        nav_toolbar.addWidget(self.reload_btn)

        # Add URL bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        nav_toolbar.addWidget(self.url_bar)

        # Create web view
        self.web_view = QWebEngineView()
        self.web_view.setUrl(QUrl('https://www.google.com'))
        self.web_view.urlChanged.connect(self.update_url)
        layout.addWidget(self.web_view)

        # Set window size and show
        self.setGeometry(100, 100, 1200, 800)
        self.show()

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        self.web_view.setUrl(QUrl(url))

    def update_url(self, url):
        self.url_bar.setText(url.toString())

    def navigate_back(self):
        self.web_view.back()

    def navigate_forward(self):
        self.web_view.forward()

    def reload_page(self):
        self.web_view.reload()

def main():
    app = QApplication(sys.argv)
    
    # Set application-wide dark palette
    dark_palette = QPalette()
    dark_palette.setColor(QPalette.ColorRole.Window, QColor(26, 26, 26))
    dark_palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))
    dark_palette.setColor(QPalette.ColorRole.Base, QColor(45, 45, 45))
    dark_palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ColorRole.Text, QColor(255, 255, 255))
    dark_palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ColorRole.ButtonText, QColor(255, 255, 255))
    dark_palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
    app.setPalette(dark_palette)
    
    browser = ExiledBrowser()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
