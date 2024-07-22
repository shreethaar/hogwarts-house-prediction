import subprocess

# Run pip freeze and get the output
result = subprocess.run(['pip3', 'freeze'], capture_output=True, text=True)
packages = result.stdout.splitlines()

# Sort packages alphabetically
sorted_packages = sorted(packages)

# Print sorted packages
for package in sorted_packages:
    print(package)

