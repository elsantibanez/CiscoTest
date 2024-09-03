
# Cisco Device Data Gatherer

A Python script designed to interact with Cisco network devices, gather various data points, and provide insights or configurations.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Overview

This project aims to automate the process of collecting data from Cisco network devices using Python. It leverages libraries like `netmiko` for SSH connections and `paramiko` for more complex interactions if needed. The script can be used for network monitoring, configuration backups, or as a foundation for more complex network management tools.

## Features

- **Device Connection:** Secure SSH connections to Cisco devices.
- **Data Collection:** Gather information like device status, interfaces, routing tables, etc.
- **Configuration Backup:** Option to save current device configurations.
- **Reporting:** Generate basic reports or logs of collected data.

## Requirements

- Python 3.6 or higher
- `netmiko` library
- `paramiko` library (optional, for more advanced SSH features)
- `pandas` for data manipulation (optional)
- `requests` for API interactions if needed (optional)

Install these with pip:

```bash
pip install netmiko paramiko pandas requests
```

## Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:yourusername/cisco-data-gatherer.git
   ```

2. Navigate to the project directory:
   ```bash
   cd cisco-data-gatherer
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script with:

```bash
python main.py
```

You can pass arguments for specific device IPs, usernames, and passwords for automation.

## Configuration

Edit `config.yaml` to include:

- Device IP addresses or hostnames
- SSH credentials
- Specific commands to run or data to collect

Example configuration:

```yaml
devices:
  - hostname: 192.168.1.1
    username: admin
    password: yourpassword
    commands:
      - show version
      - show ip interface brief
```

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request. Ensure your code follows PEP 8 and includes tests where applicable.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Cisco for their network devices and documentation.
- The `netmiko` community for simplifying network device interactions.
- Contributors on GitHub for open-source libraries and tools.

