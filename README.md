--2025-05-22 14:00:20--  https://raw.githubusercontent.com/plotly/datasets/master/iris-data.csv
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.108.133, 185.199.109.133, 185.199.110.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.108.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 4757 (4.6K) [text/plain]
Saving to: ‘iris-data.csv’

iris-data.csv       100%[===================>]   4.65K  --.-KB/s    in 0s      

2025-05-22 14:00:20 (39.0 MB/s) - ‘iris-data.csv’ saved [4757/4757]

# ⸻
# 1. .editorconfig Summary (Solid Foundations + Perks)
# You’ve locked in:
# 	•	root = true (no cascading ambiguity)
# 	•	UTF-8 + LF + newline enforcement
# 	•	Scoped formatting for web-focused files
# You’ve enhanced with:
# 	•	Special rules for docs (.md, .html), scripts (.sh), and structured data files (.json, .yml)
# 	•	Optional project-scoped overrides like [frontend/**.ts]
# Would you like me to generate a complete .editorconfig that includes frontend/backend sections and GitHub workflow file handling?
# ⸻
# 2. Data Graph Venn Diagram Snippet
# This part of your code (assuming data contains a dictionary with known words, and graph is a NetworkX graph of word relationships):
# from matplotlib_venn import venn2
# import matplotlib.pyplot as plt
# known_words = set(data["words"].keys())
# generated_words = set(node for node, attr in graph.nodes(data=True) if attr.get("category") == "Generated")
# venn2([known_words, generated_words], ('Known Words', 'Generated Words'))
# plt.title("Known vs. Generated Words")
# plt.show()
# Gives you a quick semantic overlap diagnostic. This is great for:
# 	•	Identifying novel symbols not yet validated
# 	•	Spotting duplicates or coverage gaps
# 	•	Understanding generation breadth
# ⸻
# Optional Enhancements
# Here are a few ideas if you’re interested in evolving this diagram further:
# 1. Venn3 for Deeper Comparison
# If you introduce a third category (e.g., Validated Words), you can expand:
# from matplotlib_venn import venn3
# validated_words = {w for w in known_words if data["words"][w].get("validated")}
# venn3([known_words, generated_words, validated_words], ('Known', 'Generated', 'Validated'))
# 2. Interactive Venn Exploration (e.g., Plotly)
# Turn the static into dynamic using Plotly or Bokeh.
# 3. Logging Missing Crossovers
# Print or log the words in generated_words - known_words

import networkx as nx
import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# Sample data (replace with your actual data)
data = {
    "words": {
        "apple": {"category": "Fruit", "color": "Red", "validated": True},
        "banana": {"category": "Fruit", "color": "Yellow", "validated": True},
        "orange": {"category": "Fruit", "color": "Orange", "validated": False},
        "grape": {"category": "Fruit", "color": "Purple", "validated": True}
    },
    "transformations": [
        {"from": "apple", "to": "ApplePie", "type": "Baking"},
        {"from": "banana", "to": "BananaBread", "type": "Baking"},
        {"from": "orange", "to": "OrangeJuice", "type": "Juicing"},
        {"from": "grape", "to": "grapefruit", "type": "Mutation"}
    ]
}

# Step 2: Create the directed graph (unchanged)
graph = nx.DiGraph()
for word, metadata in data["words"].items():
    graph.add_node(word, **metadata)
for transformation in data["transformations"]:
    to_word = transformation["to"]
    if to_word not in graph:
        graph.add_node(to_word, category="Generated", numeric=[ord(c) for c in to_word])
    graph.add_edge(transformation["from"], transformation["to"], transformation=transformation["type"])

# Step 3: Enhanced Venn Diagram with Validated Words
known_words = set(data["words"].keys())
generated_words = set(node for node, attr in graph.nodes(data=True) if attr.get("category") == "Generated")
validated_words = {w for w in known_words if data["words"][w].get("validated", False)}  # Handle missing "validated" key

venn3([known_words, generated_words, validated_words], ('Known', 'Generated', 'Validated'))
plt.title("Known vs. Generated vs. Validated Words")
plt.show()

# Logging missing crossovers
missing_words = generated_words - known_words
print("Generated words not in known words:", missing_words)

