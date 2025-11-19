import yaml
import sys

def load_devices(path="configs/devices.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def main():
    try:
        data = load_devices()
    except FileNotFoundError:
        print("Error: configs/devices.yaml not found", file=sys.stderr)
        sys.exit(2)

    devices = data.get("devices", [])
    print("Connected devices:")
    for d in devices:
        print(f"- {d.get('name')} ({d.get('ip')}) - {d.get('vendor')}")

if __name__ == "__main__":
    main()

