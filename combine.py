import os

# Paths
source_config_file = "BH.cfg"  # The original config file
output_config_file = "bh_combined.cfg"  # The new combined config file
filter_folder = "filter-blocks"
files_to_append = [
    "amazon.bh", "assassin.bh", "barbarian.bh", "druid.bh",
    "leveling.bh", "necromancer.bh", "paladin.bh", "sorceress.bh"
]

start_marker = "//////////////////////////////////////////////////////////////////\n// START FILTER BLOCKS\n//////////////////////////////////////////////////////////////////"
end_marker = "//////////////////////////////////////////////////////////////////\n// END FILTER BLOCKS\n//////////////////////////////////////////////////////////////////"


def append_filter_blocks(source_content, filter_blocks):
    """Inserts filter blocks between start and end markers."""
    before_start, after_end = source_content.split(start_marker, 1)
    after_start, after_end = after_end.split(end_marker, 1)
    
    # Combine content
    combined_content = (
        before_start + start_marker + "\n\n" +
        filter_blocks + "\n" +
        end_marker + after_end
    )
    return combined_content


def main():
    # Check if the source config file exists
    if not os.path.exists(source_config_file):
        print(f"Error: {source_config_file} not found.")
        return

    # Read the source config file
    with open(source_config_file, "r") as f:
        source_content = f.read()

    # Ensure both markers exist
    if start_marker not in source_content or end_marker not in source_content:
        print(f"Error: Missing start or end marker in {source_config_file}.")
        return

    # Check if the filter folder exists
    if not os.path.isdir(filter_folder):
        print(f"Error: Folder '{filter_folder}' not found.")
        return

    # Collect content from the files to append
    filter_blocks = ""
    for filename in files_to_append:
        file_path = os.path.join(filter_folder, filename)
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                filter_blocks += f.read() + "\n"
            print(f"Appended {filename} to filter blocks.")
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
            filter_blocks += f.read() + "\n"
        print(f"Appended {runes_file} to filter blocks.")
    else:
        print(f"Error: {runes_file} not found in {filter_folder}.")
        return

    # Combine the source content with the filter blocks
    combined_content = append_filter_blocks(source_content, filter_blocks)

    # Write the combined content to the output file
    with open(output_config_file, "w") as f:
        f.write(combined_content)

    print(f"Done! Combined config saved as {output_config_file}.")


if __name__ == "__main__":
    main()
