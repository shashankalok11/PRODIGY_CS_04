# Keylogger with GUI

This is a basic keylogger application with a graphical user interface (GUI) implemented in Python. The application records keystrokes and saves them to a log file, and provides functionality to start, stop, and view the keylog file through the GUI.

## Features

- **Start**: Begins logging keystrokes.
- **Stop**: Stops logging keystrokes.
- **View Log**: Opens a new window to display the contents of the keylog file.

## Requirements

- Python 3.x
- `pynput` library
- `tkinter` (included with Python standard library)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd your-repository
   ```

3. **Install Dependencies**:
   Ensure you have `pynput` installed. If not, install it using pip:
   ```bash
   pip install pynput
   ```

## Usage

1. **Run the Application**:
   ```bash
   python keylogger_gui.py
   ```

2. **GUI Controls**:
   - **Start**: Click this button to begin recording keystrokes.
   - **Stop**: Click this button to stop recording keystrokes.
   - **View Log**: Click this button to open a new window displaying the recorded keystrokes.

## Ethical Considerations

- **Consent**: Ensure you have explicit permission from all users whose keystrokes will be logged.
- **Transparency**: Inform users about the keylogger and its purpose.
- **Legal Compliance**: Follow legal regulations and data privacy laws applicable to keylogging.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- The `pynput` library for capturing keyboard events.
- The `tkinter` library for creating the GUI.
