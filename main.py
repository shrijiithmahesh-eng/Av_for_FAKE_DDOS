import os

# The DNA of the "EngineRipper" virus
VIRUS_DNA = ["riny", "pbzcvyr", "onfr64", "o64qrpbqr", "os.environ"]

def apply_cure(directory):
    print(f"🛡️  HackMe-Guard: Scanning {directory} for infections...")
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                with open(path, 'r') as f:
                    content = f.read()
                    # Check for the secret ROT13 signatures you found!
                    if any(dna in content for dna in VIRUS_DNA):
                        print(f"🛑 CRITICAL: Infection found in {file}!")
                        print(f"🔒 QUARANTINING: Moving {file} to safe vault...")
                        os.rename(path, path + ".INFECTED")
                    else:
                        print(f"✅ {file} passed the Architect's test.")

# Run the cure on your lab folder
# apply_cure("./my_lab_scripts")