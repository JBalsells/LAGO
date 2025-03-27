import sys
import yaml
import paramiko

with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

def ssh_connect(command):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(
            hostname=config["connection"]["host"], 
            username=config["connection"]["user"], 
            password=config["connection"]["password"]
            )
        
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode()
        error = stderr.read().decode()
        
        client.close()
        
        return output if output else error
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    script_name = sys.argv[0]
    command_name = sys.argv[1]
    value = sys.argv[2]

    if command_name == "high_voltage":
        command = "-s hv1"
    elif command_name == "threshold":
        command = "-s t1"
    elif command_name == "get_registers":
        command = "-a"
    elif command_name == "get_data":
        command = "-o"

    command = f"./lago {command} {value}"
    print(f"{command}: {value}")
    print(ssh_connect(command))
