# prompt: Great — that output shows the tips are being printed correctly, so the method is now defined and working.
# Just to confirm, your working class likely looks something like this:
# class CopilotUsageGuide:
#     def __init__(self):
#         self.tips = [
#             "Use clear and concise prompts.",
#             "Ask specific questions for better answers.",
#             "Iterate and refine your prompt if needed.",
#         ]
#     def print_guide(self):
#         for tip in self.tips:
#             print(f"- {tip}")
# And you’re running:
# def run_guide():
#     guide = CopilotUsageGuide()
#     guide.print_guide()
# run_guide()
# If that’s the structure you have now, you’re all set! Let me know if you’d like to expand this guide with categories, interactive input, or formatting (like markdown in notebooks).

class CopilotUsageGuide:
    def __init__(self):
        self.tips = [
            "Use clear and concise prompts.",
            "Ask specific questions for better answers.",
            "Iterate and refine your prompt if needed.",
        ]

    def print_guide(self):
        for tip in self.tips:
            print(f"- {tip}")

    def print_guide_with_markdown(self):
      for tip in self.tips:
        print(f"- {tip}")


def run_guide():
    guide = CopilotUsageGuide()
    guide.print_guide()

# Example of expanding with categories (dictionary)
def run_guide_with_categories():
    guide = CopilotUsageGuide()
    guide_categories = {
        "General Tips": [
            "Use clear and concise prompts.",
            "Ask specific questions for better answers.",
            "Iterate and refine your prompt if needed."
        ],
        "Advanced Techniques": [
            "Provide context for better understanding.",
            "Use code examples for more accurate results.",
            "Experiment with different prompt structures."
        ]
    }

    for category, tips in guide_categories.items():
        print(f"## {category}")
        for tip in tips:
            print(f"- {tip}")


# Example of interactive input
def run_interactive_guide():
    guide = CopilotUsageGuide()
    user_input = input("Enter a topic to get tips on: ")
    print(f"Tips related to {user_input}:")
    # Logic for filtering tips based on user input goes here (Currently prints all)
    for tip in guide.tips:
        print(f"- {tip}")


#Run different versions
#run_guide()
#run_guide_with_categories()
run_interactive_guide()
