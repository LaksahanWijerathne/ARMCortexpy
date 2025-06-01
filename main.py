from PyQt5.QtWidgets import (QMainWindow, QStatusBar, QAction, QDockWidget, 
                            QTreeWidget, QPlainTextEdit, QApplication, 
                            QSplitter, QToolBar, QLabel, QVBoxLayout, QWidget,QTreeWidgetItem)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import sys
import os

class ARMCortexpyIDE(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.create_actions()
        self.create_menus()
        self.create_toolbars()
        self.create_statusbar()
        self.create_dock_widgets()
        
    def setup_ui(self):
        self.setWindowTitle("ARMCortexpy IDE")
        self.resize(1200, 800)
        
        # Central Widget with Splitter
        self.central_splitter = QSplitter(Qt.Horizontal)
        self.setCentralWidget(self.central_splitter)
        
        # Project Explorer (Left Dock)
        self.project_tree = QTreeWidget()
        self.project_tree.setHeaderLabel("Project")
        
        # Code Editor (Center)
        self.editor = QPlainTextEdit()  # Will replace with QsciScintilla later
        self.editor.setStyleSheet("font-family: Consolas; font-size: 12pt;")
        
        # Peripheral Config (Right Dock)
        self.periph_config = QTreeWidget()
        self.periph_config.setHeaderLabel("Peripherals")
        
        # Output Console (Bottom Dock)
        self.output_console = QPlainTextEdit()
        self.output_console.setReadOnly(True)
        
        # Add widgets to splitter
        self.central_splitter.addWidget(self.project_tree)
        self.central_splitter.addWidget(self.editor)
        self.central_splitter.setSizes([200, 600])
        
    def create_actions(self):
        # File Actions
        self.new_action = QAction(QIcon.fromTheme("document-new"), "&New Project", self)
        self.open_action = QAction(QIcon.fromTheme("document-open"), "&Open", self)
        self.save_action = QAction(QIcon.fromTheme("document-save"), "&Save", self)
        
        # Build Actions
        self.build_action = QAction(QIcon.fromTheme("run-build"), "&Build", self)
        self.flash_action = QAction(QIcon.fromTheme("media-playback-start"), "&Flash", self)
        
        # Debug Actions
        self.debug_action = QAction(QIcon.fromTheme("debug-run"), "&Debug", self)
        
    def create_menus(self):
        menubar = self.menuBar()
        
        # File Menu
        file_menu = menubar.addMenu("&File")
        file_menu.addAction(self.new_action)
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)
        
        # Build Menu
        build_menu = menubar.addMenu("&Build")
        build_menu.addAction(self.build_action)
        build_menu.addAction(self.flash_action)
        
        # Debug Menu
        debug_menu = menubar.addMenu("&Debug")
        debug_menu.addAction(self.debug_action)
        
    def create_toolbars(self):
        # Main Toolbar
        self.toolbar = self.addToolBar("Main")
        self.toolbar.setMovable(False)
        
        self.toolbar.addAction(self.new_action)
        self.toolbar.addAction(self.open_action)
        self.toolbar.addAction(self.save_action)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.build_action)
        self.toolbar.addAction(self.flash_action)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.debug_action)
        
        # MCU Status Widget
        self.mcu_status = QLabel("STM32F411 ● Disconnected")
        self.toolbar.addWidget(self.mcu_status)
        
    def create_statusbar(self):
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)
        self.statusbar.showMessage("Ready")
        
        # Permanent widgets
        self.line_col_label = QLabel("Ln 1, Col 1")
        self.statusbar.addPermanentWidget(self.line_col_label)
        
    def create_dock_widgets(self):
        # Peripheral Config Dock (Right)
        periph_dock = QDockWidget("Peripheral Configuration", self)
        periph_dock.setWidget(self.periph_config)
        periph_dock.setAllowedAreas(Qt.RightDockWidgetArea)
        self.addDockWidget(Qt.RightDockWidgetArea, periph_dock)
        
        # Output Console Dock (Bottom)
        output_dock = QDockWidget("Output", self)
        output_dock.setWidget(self.output_console)
        output_dock.setAllowedAreas(Qt.BottomDockWidgetArea)
        self.addDockWidget(Qt.BottomDockWidgetArea, output_dock)
        
    def load_demo_project(self):
        """For testing UI layout"""
        self.project_tree.clear()
        root = self.project_tree.invisibleRootItem()
        
        # Add demo items
        project_item = QTreeWidgetItem(["ARMCortexpy Demo"])
        src_item = QTreeWidgetItem(["src"])
        src_item.addChild(QTreeWidgetItem(["main.acpy"]))
        src_item.addChild(QTreeWidgetItem(["hal_config.acpy"]))
        
        project_item.addChild(src_item)
        project_item.addChild(QTreeWidgetItem(["STM32F411.ioc"]))
        root.addChild(project_item)
        
        # Add peripheral demo
        periph_root = self.periph_config.invisibleRootItem()
        uart_item = QTreeWidgetItem(["UART2"])
        uart_item.addChild(QTreeWidgetItem(["Baud: 115200"]))
        uart_item.addChild(QTreeWidgetItem(["Mode: Full Duplex"]))
        
        gpio_item = QTreeWidgetItem(["GPIO"])
        gpio_item.addChild(QTreeWidgetItem(["PA5: LED_OUT"]))
        gpio_item.addChild(QTreeWidgetItem(["PC13: BUTTON_IN"]))
        
        periph_root.addChild(uart_item)
        periph_root.addChild(gpio_item)
        
        # Demo editor content
        self.editor.setPlainText(
            "# ARMCortexpy Demo\n"
            "import armcortexpy.stm32 as stm\n\n"
            "led = stm.GPIO('PA5', stm.OUT)\n"
            "button = stm.GPIO('PC13', stm.IN)\n\n"
            "def main():\n"
            "    while True:\n"
            "        if button.read():\n"
            "            led.toggle()\n"
            "        stm.delay(200.ms)"
        )

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("ARMCortexpy IDE")
    app.setApplicationVersion("0.0.1")
    
    # Set style (optional)
    app.setStyle('Fusion')
    
    window = ARMCortexpyIDE()
    window.load_demo_project()  # Remove in production
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()