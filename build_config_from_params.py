from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/merge-files', methods=['POST'])
def merge_files():
    data = request.json
    rune_design = data.get('rune_design')

    if rune_design not in ['cosmic-rainbow', 'classic']:
        return jsonify({"error": "Invalid rune_design parameter"}), 400

    base_url = "https://raw.githubusercontent.com/DoctorWoot420/cosmic-resurgence-bh/main/new-temp/BH_cosmic.cfg"
    if rune_design == 'cosmic-rainbow':
        block_url = "https://raw.githubusercontent.com/DoctorWoot420/cosmic-resurgence-bh/main/new-temp/filter-blocks/runes-cosmic-rainbow.bh"
    else:
        block_url = "https://raw.githubusercontent.com/DoctorWoot420/cosmic-resurgence-bh/main/new-temp/filter-blocks/runes-classic.bh"

    # Fetch base file
    base_response = requests.get(base_url)
    if base_response.status_code != 200:
        return jsonify({"error": "Failed to fetch base file"}), 400
    base_content = base_response.text

    # Fetch block file
    block_response = requests.get(block_url)
    if block_response.status_code != 200:
        return jsonify({"error": f"Failed to fetch block file for {rune_design}"}), 400
    block_content = block_response.text

    # Insert block content into base content
    base_lines = base_content.splitlines()
    insert_index = None
    for i, line in enumerate(base_lines):
        if "// start runes block" in line.lower():
            insert_index = i + 3
            break

    if insert_index is None:
        return jsonify({"error": "Indicator '// START RUNES BLOCK' not found in base file"}), 400

    merged_lines = base_lines[:insert_index] + block_content.splitlines() + base_lines[insert_index:]
    merged_content = "\n".join(merged_lines)

    return merged_content

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8083)
