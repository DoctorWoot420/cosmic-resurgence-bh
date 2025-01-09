import os

# Paths
source_config_file = "BH.cfg"  # The original config file
output_config_file = "bh_combined.cfg"  # The new combined config file
filter_folder = "filter-blocks"
files_to_append = [
    "amazon.bh", "assassin.bh", "barbarian.bh", "druid.bh",
    "leveling.bh", "necromancer.bh", "paladin.bh", "sorceress.bh"
]

def append_to_file(file_path, content):
    """Appends content to the given file."""
    with open(file_path, "a") as f:
        f.write(content + "\n")

def main():
    # Check if the source config file exists
    if not os.path.exists(source_config_file):
        print(f"Error: {source_config_file} not found.")
        return

    # Create or overwrite the combined output file
    with open(output_config_file, "w") as f:
        with open(source_config_file, "r") as source:
            f.write(source.read())
        f.write("\n")  # Add a blank line for separation

    print(f"Copied {source_config_file} to {output_config_file}.")

    # Check if filter folder exists
    if not os.path.isdir(filter_folder):
        print(f"Error: Folder '{filter_folder}' not found.")
        return

    # Append each file's content
    for filename in files_to_append:
        file_path = os.path.join(filter_folder, filename)
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                content = f.read()
            append_to_file(output_config_file, content)
            print(f"Appended {filename} to {output_config_file}.")
        else:
            print(f"Warning: {filename} not found in {filter_folder}. Skipping.")

    # Ask for runes file selection
    print("Choose a runes file to append:")
    print("1. runes-classic.bh")
    print("2. runes-cosmic-rainbow.bh")
    choice = input("Enter 1 or 2: ").strip()

    runes_file = None
    if choice == "1":
        runes_file = "runes-classic.bh"
    elif choice == "2":
        runes_file = "runes-cosmic-rainbow.bh"
    else:
        print("Invalid choice. Exiting.")
        return

    # Append the chosen runes file
    runes_path = os.path.join(filter_folder, runes_file)
    if os.path.exists(runes_path):
        with open(runes_path, "r") as f:
            content = f.read()
        append_to_file(output_config_file, content)
        print(f"Appended {runes_file} to {output_config_file}.")
    else:
        print(f"Error: {runes_file} not found in {filter_folder}.")

    print(f"Done! Combined config saved as {output_config_file}.")

if __name__ == "__main__":
    main()
