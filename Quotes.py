import random

quotes = [
    "If something seems stupid but if it works, then it isn't stupid.",
    "First rule of programming: If it works, don’t touch it.",
    "Use your brain when coding, you can't just type something and expect it to work.",
    "Python is a very simple language and it's great for learning how to code.",
    "ChatGPT is a programmer's best friend.",
    "Coding is very fun to do once you have the knowledge for it.",
    "People that want to learn python should use the Python Crash Course book by Eric Matthes.",
    "There are a lot of coding languages, python is just one of many.",
    "Every programmer has that one language that makes them think: 'Man, what the fuck is this?'",
    "Experience is the name everyone gives to their mistakes.",
    "The best error message is the one that never shows up.",
    "Any fool can write code that a computer can understand. Good programmers write code that humans can understand.",
    "There are only two kinds of programming languages: those people always bitch about and those nobody uses.",
    "If debugging is the process of removing bugs, then programming must be the process of putting them in.",
    "The most disastrous thing that you can ever learn is your first programming language.",
    "Saying that Java is good because it works on all platforms is like saying anal sex is good because it works on all genders.",
    "There is always one more bug to fix.",
    "Software testing is a sport like hunting, it's bughunting.",
    "If you don’t make mistakes, you’re not working on hard enough problems. And that’s a big mistake.",
    "Any sufficiently advanced bug is indistinguishable from a feature.",
    "Coding is 90% figuring out why it doesn’t work and 10% writing code that doesn’t work.",
    "My code doesn’t work. I have no idea why. My code works. I have no idea why.",
    "The best part about programming is the triumph of fixing a bug after hours of frustration. The worst part is that the fix was one character.",
    "Software and cathedrals are much the same – first we build them, then we pray",
    "Code is like humor. When you have to explain it, it’s bad.",
    "Programming is like sex: one mistake and you have to support it for the rest of your life.",
    "Programming today is a race between software engineers striving to build bigger and better idiot-proof programs, and the Universe trying to produce bigger and better idiots.",
    "If your code looks like it was written by a drunken raccoon, congratulations, you’re a real programmer.",
    "Sometimes the best way to fix a bug is to just delete the entire module and start over. Crying is optional.",
    "If your software needs documentation longer than the code itself, you’ve fucked up.",
    "The best developers write code nobody can understand so they don’t have to explain it.",
    "Git commit messages should be brutally honest. ‘Fixed shit’ is a classic.",
    "There are two kinds of programmers: those who can write code that works, and those who can debug code that doesn’t.",
    "The best bug is the one you never have to fix because someone else's code is so bad it breaks first.",
    "Programming is 90% figuring out how to Google the error message.",
    "Refactoring: turning your spaghetti code into lasagna — layers of pain baked in sauce.",
    "The biggest lie in software development: 'This will only take five minutes.'",
    "You don’t fix bugs; you just move them around until they land on someone else’s desk.",
    "The best way to get a project done faster is to start sooner… or just blame the deadline.",
    "Your code doesn’t have to be perfect, it just has to work… until the next deadline.",
    "If you want to impress a programmer, just show up with a debugger.",
    "If at first you don’t succeed; call it version 1.0.",
    "I’m not lazy, I’m just very good at doing nothing until something breaks.",
    "Why do Java developers wear glasses? Because they don’t see sharp.",
    "If your code is working, you’re not coding hard enough."
]

def get_random_quote():
    return random.choice(quotes)

if __name__ == "__main__":
    for i in range(1, 6):  # Print 5 quotes
        print(f"\nQuote {i}:")
        print(get_random_quote())
