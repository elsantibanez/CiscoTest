import os
import yaml
from gather_data import collect_data
from backup_config import backup_configuration
from reporting import generate_report

def load_config(config_file='config.yaml'):
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)

    # Read credentials from environment variables
    for device in config['devices']:
        device['username'] = os.getenv('DEVICE_USERNAME')
        device['password'] = os.getenv('DEVICE_PASSWORD')
        if device['username'] is None or device['password'] is None:
            raise ValueError("Device credentials not found in environment variables.")

    return config

def main():
    try:
        config = load_config()
    except ValueError as e:
        print(f"Error: {e}")
        return

    for device in config['devices']:
        hostname = device['hostname']
        username = device['username']
        password = device['password']
        commands = device['commands']

        # Data collection
        data = collect_data(hostname, username, password, commands)

        # Backup configuration
        backup_configuration(hostname, username, password)

        # Generate report
        generate_report(hostname, data)

if __name__ == '__main__':
    main()