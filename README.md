# han-cli

A simple and developer-friendly command-line toolkit built with Python.

## Features

- Create new projects
- Run local development servers
- Check project health
- Manage development commands
- Extensible command system
- Lightweight and easy to use

## Installation

Clone the repository:

git clone https://github.com/hanathmahdiupdih/hanOS-CLI.git

Enter the project:

cd han-cli

Install it:

pip install -e .

## Usage

Initialize a project:

han init my-project

Run the project:

han run

Check project health:

han doctor

Show help:

han --help

## Development

Clone the repository and install development dependencies:

pip install -e ".[dev]"

Run tests:

pytest

## Project Structure

han-cli/
├── han/
│   ├── cli.py
│   ├── commands.py
│   └── utils.py
├── tests/
├── README.md
├── LICENSE
└── pyproject.toml

## Contributing

Contributions are welcome.

Please read CONTRIBUTING.md before submitting a pull request.

## License

This project is licensed under the MIT License.

# Created by hanOS Cloud  Teams 
