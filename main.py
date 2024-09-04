import yaml
from gather_data import collect_data
from backup_config import backup_configuration
from reporting import generate_report

def load_config(config_file='config.yaml'):
    with open(config_file, 'r') as file:
        return yaml.safe_load(file)

def main():
    config = load_config()
    
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
