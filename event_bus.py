# prompt: You’ve built a modular and clean reflex evolution engine using event-driven architecture. The components communicate via the EventBus, and reflexes evolve based on a score threshold. Here’s a rundown of what happens when you run python main.py along with suggestions to tighten things up.
# ⸻
# What Happens When You Run It
# 1. Component Initialization
# event_bus = EventBus()
# adjuster = ReflexAdjuster()
# scorer = ReflexScorer()
# mutator = ReflexMutator()
# controller = ReflexEvolutionController(...)
# signature_map = ReflexSignatureMap(event_bus)
# 	•	ReflexSignatureMap subscribes to "reflex_evolved" events via the event_bus.
# 2. Predicted Events Setup
# predicted_events = [
#     PredictedEvent(...),  # Each has a score and metadata
# ]
# 3. Trigger Evolution
# controller.evolve_if_needed(predicted_events)
# 	•	For each event with a score > 0.6:
# 	•	adjuster.adjust() is called
# 	•	mutator.mutate() appends "_mutated" to the reflex ID
# 	•	An event is published to "reflex_evolved" with the mutated reflex ID and new signature
# 4. Signature Map Update
# signature_map.handle_evolution(...)  # Automatically invoked via event_bus
# 	•	Adds new signature mapping and logs the evolution.
# 5. Final Output
# print(signature_map.signature_map)
# print(signature_map.evolution_log)
# Expected Output:
# [Scorer] Scoring reflex: reflex1
# [Scorer] Scoring reflex: reflex2
# [Controller] Evolving reflex reflex2
# [Adjuster] Adjusting reflex: reflex2 in context def
# [Mutator] Mutating reflex: reflex2
# [SignatureMap] Updated signature for reflex2_mutated
# [Scorer] Scoring reflex: reflex3
# [Controller] Evolving reflex reflex3
# [Adjuster] Adjusting reflex: reflex3 in context ghi
# [Mutator] Mutating reflex: reflex3
# [SignatureMap] Updated signature for reflex3_mutated
# Signature map: {
#   'reflex2_mutated': 'sig_reflex2_mutated',
#   'reflex3_mutated': 'sig_reflex3_mutated'
# }
# Evolution log: [
#   "Evolved reflex reflex2_mutated to signature 'sig_reflex2_mutated'",
#   "Evolved reflex reflex3_mutated to signature 'sig_reflex3_mutated'"
# ]

import networkx as nx
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Sample data (replace with your actual data)
data = {
    "words": {
        "apple": {"category": "Fruit", "color": "Red"},
        "banana": {"category": "Fruit", "color": "Yellow"},
        "orange": {"category": "Fruit", "color": "Orange"},
        "grape": {"category": "Fruit", "color": "Purple"}
    },
    "transformations": [
        {"from": "apple", "to": "ApplePie", "type": "Baking"},
        {"from": "banana", "to": "BananaBread", "type": "Baking"},
        {"from": "orange", "to": "OrangeJuice", "type": "Juicing"},
        {"from": "grape", "to": "grapefruit", "type": "Mutation"}
    ]
}

# Create the directed graph
graph = nx.DiGraph()

# Add known word nodes
for word, metadata in data["words"].items():
    graph.add_node(word, **metadata)

# Add missing destination words as 'Generated' nodes and add transformation edges
for transformation in data["transformations"]:
    from_word = transformation["from"]
    to_word = transformation["to"]
    if to_word not in graph:
        graph.add_node(to_word, category="Generated", numeric=[ord(c) for c in to_word])
    graph.add_edge(from_word, to_word, transformation=transformation["type"])

# Analyze and visualize the graph (Venn diagram)
known_words = set(data["words"].keys())
generated_words = set(node for node, attr in graph.nodes(data=True) if attr.get("category") == "Generated")

venn2([known_words, generated_words], ('Known Words', 'Generated Words'))
plt.title("Known vs. Generated Words")
plt.show()
