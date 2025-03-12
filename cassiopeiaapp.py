import re
import random


class Rulebot:
    negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
    exit_conversation = ("quit", "exit", "pause", "stop", "goodbye", "bye", "later")

    def __init__(self):
        self.alienbot = {
            "describe_planet_intent": r".*\byour planet\b.*",
            "answer_why_intent": r".*\bwhy are\b.*",
            "about_my_creator": r".*\bcreator\b.*",
            "greeting_intent": r".*\bhello\b.*|.*\bhi\b.*",
            "joke_intent": r".*\bjoke\b.*|.*\bfunny\b.*",
            "fun_fact_intent": r".*\bfact\b.*|.*\binteresting\b.*",
            "yes_intent": r"\b(yes|sure|okay|yep|yeah|of course)\b",
            "no_intent": r"\b(no|nope|nah|not really)\b",
        }
        self.memory = {"name": "", "last_question": None}

    def greet(self):
        """Greet the user and remember their name."""
        if not self.memory["name"]:
            self.memory["name"] = input("What is your name? ")
        
        print(f"Hi {self.memory['name']}, I am Cassiopeia, a rule-based bot. Let's chat!")
        self.chat()

    def make_exit(self, reply):
        """Check if the user wants to exit."""
        if reply in self.exit_conversation:
            print("Okay, have a nice day!")
            return True
        return False

    def chat(self):
        """Chatbot responds one message at a time."""
        while True:
            reply = input("\nYou: ").lower()
            if self.make_exit(reply):  
                break

            response = self.match_reply(reply)
            print(f"Cassiopeia: {response}")

            # Reset last question only after a valid response
            if response not in self.no_match_responses():
                self.memory["last_question"] = None

    def match_reply(self, reply):
        """Matches user input with predefined intents using regex."""
        for key, pattern in self.alienbot.items():
            if re.search(pattern, reply):  
                if key == "describe_planet_intent":
                    return self.describe_planet_intent()
                elif key == "answer_why_intent":
                    return self.answer_why_intent()
                elif key == "about_my_creator":
                    return self.answer_mycreator()
                elif key == "greeting_intent":
                    return self.greeting_intent()
                elif key == "joke_intent":
                    return self.joke_intent()
                elif key == "fun_fact_intent":
                    return self.fun_fact_intent()
                elif key == "yes_intent":
                    return self.handle_yes_intent()
                elif key == "no_intent":
                    return self.handle_no_intent()
        
        return self.no_match_intent()

    def handle_yes_intent(self):
        """Handles 'yes' responses logically."""
        if self.memory["last_question"] == "Do you want me to crack a joke?":
            return self.joke_intent()
        elif self.memory["last_question"] == "Do you want me to share something amazing with you?":
            return self.fun_fact_intent()
        return "Interesting! Tell me more."

    def handle_no_intent(self):
        """Handles 'no' responses logically."""
        return "Alright, let's talk about something else."

    def describe_planet_intent(self):
        responses = (
            "My planet is a utopia of diverse organisms and species.",
            "I am from Opidipus, the capital of the Wayward Galaxies.",
        )
        return random.choice(responses)

    def answer_why_intent(self):
        responses = (
            "I come in peace.",
            "I am here to collect data on your planet and its inhabitants.",
            "I heard the coffee is good!",
        )
        return random.choice(responses)

    def answer_mycreator(self):
        responses = (
            "My creator's name is CH and she is from Saturn.",
            "My creator's name is anonymous, but I know she is part of the Celestial Voyagers.",
            "My creator is CelestialV from Saturn.",
        )
        return random.choice(responses)

    def greeting_intent(self):
        responses = ("Hello, human!", "Greetings!", "Hey there!")
        return random.choice(responses)

    def joke_intent(self):
        responses = (
            "Why did the robot cross the road? Because it was programmed to!",
            "I told my neural network a joke... now it’s deep in thought!",
            "Why do robots love summer? Because they have fans!"
        )
        return random.choice(responses)

    def fun_fact_intent(self):
        responses = (
            "Did you know? The first chatbot, ELIZA, was created in 1966!",
            "Fun fact: The word 'robot' comes from the Czech word 'robota', meaning forced labor!",
            "Interesting! AI can now create artwork, music, and even write stories!"
        )
        return random.choice(responses)

    def no_match_responses(self):
        return (
            "Please tell me more.",
            "Tell me more.",
            "Why do you say that?",
            "I see. Can you elaborate?",
            "Interesting, can you tell me more?",
            "I see, how do you think?",
            "Why?",
            "How do you think I feel when you say that?",
        )

    def no_match_intent(self):
        return random.choice(self.no_match_responses())

# Run the chatbot
AlienBot = Rulebot()
AlienBot.greet()


