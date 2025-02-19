import time

def display_section(title, text):
    print(f"\n\033[1m{title}\033[0m")  # Bold title
    print(text)
    time.sleep(1)

def journaling_prompt(prompt, file):
    print("\n\033[94mReflection Prompt:\033[0m")  # Blue-colored text
    print(prompt)
    try:
        response = input("\n(Press Enter to write your response...)\n")
        file.write(f"{prompt}\n{response}\n\n")
    except Exception as e:
        print(f"An error occurred while capturing your response: {e}")

# Therapy session structure
session_data = [
    {
        "title": "CLIENT",
        "text": "I don’t even know how I feel. Pissed, yeah, but also… I don’t know. Stupid? Embarrassed? Like, why do I even care this much?",
        "assistant": "When you shared that you didn’t know how you felt, it sounded like a whirlwind of emotions had been swirling inside you. We explored these feelings together during our session. Can you recall which thoughts were linked to feeling stupid or embarrassed?",
        "prompt": "What specific thoughts or fears arose for you when you felt embarrassed or stupid?"
    },
    {
        "title": "CLIENT",
        "text": "I was at the bar, right? And they kept texting me—'Be there soon,' 'Just parking'—and then… nothing. No call, no explanation. I sat there for almost an hour, checking my phone like an idiot.",
        "assistant": "When you recounted the experience of waiting at the bar, it seemed so painful and frustrating. During our session, we talked about comforting yourself using Dialectical Behavior Therapy (DBT) techniques. How might you have soothed yourself at that moment of waiting?",
        "prompt": "What are some nurturing activities you can recall practicing when feeling anxious or exposed?"
    },
    {
        "title": "CLIENT",
        "text": "And it’s not just this one time. It’s the pattern. I always feel like I’m reaching out more, like I have to be the one who cares more. And then I start wondering—am I just not worth showing up for?",
        "assistant": "When you noticed this pattern, we gently explored the underlying beliefs about self-worth that often accompany it. Remember, we looked at evidence during our session that challenges the belief that you're not worth showing up for. What examples can you recall of being valued by others?",
        "prompt": "List some heartfelt examples where others showed they value you and your time."
    },
    {
        "title": "CLIENT",
        "text": "It reminds me of my dad. He used to do that. Say he was coming to pick me up, and then just… not. I’d sit by the window, waiting, pretending I didn’t care.",
        "assistant": "As you shared memories of your dad, it seemed like they still carried a tender impact. During our session, we acknowledged how these past experiences relate to your current feelings. How do these memories continue to touch your feelings of being let down today?",
        "prompt": "How might acknowledging the impact of these past experiences help you in moving forward?"
    },
    {
        "title": "CLIENT",
        "text": "And now here I am, grown, sitting in a bar, still waiting. Still pretending I don’t care.",
        "assistant": "When you described this scenario, it seemed like you were repeating familiar patterns. During our session, we gently explored how to take steps to express your true emotions. What feelings were you hiding, and how can you begin expressing them more authentically?",
        "prompt": "What steps can you take to express your genuine feelings and allow yourself to be seen?"
    }
]

# Open a file to save journaling responses
with open("journaling_responses.txt", "w") as file:
    # Display session and journaling prompts
    for section in session_data:
        display_section(section["title"], section["text"])
        display_section("AI ASSISTANT", section["assistant"])
        journaling_prompt(section["prompt"], file)

    # Conclusion prompts
    conclusion_prompts = [
        "What new insight did you gain from our session together?",
        "How can the techniques we discussed support you in future situations?",
        "What support do you need to feel more secure in your relationships as you move forward?"
    ]

    print("\n\033[1mConclusion & Intentional Reflection Questions:\033[0m")
    for prompt in conclusion_prompts:
        journaling_prompt(prompt, file)

print("\n\033[92mYour responses are valuable. Take your time and reflect deeply.\033[0m")  # Green text for encouragement