import nltk
from nltk.chat.util import Chat, reflections
import pickle

pairs = [
    [
        r"I feel (.*)",
        [
            "Why do you feel %1?",
            "Oh, feeling %1 can be... something, I guess.",
            "Hmm, that's interesting. Let's focus on that feeling of %1, or maybe not!",
        ]
    ],
    [
        r"I'm (.*) (tired|sad|anxious|stressed|happy|angry)",
        [
            "Have you tried... not being %2?",
            "Wow, %2, that's something.",
            "Hmm, what if you were, like, the opposite of %2? Ever thought about that?",
        ]
    ],
    [
        r"why (do I|am I) (.*)",
        [
            "Oh, the classic 'why' question. Nobody knows!",
            "Good question! The universe might have an answer... but I sure don't.",
            "Why indeed! Some say it's because... well, never mind.",
        ]
    ],
    [
        r"should I (.*)",
        [
            "Probably! Or maybe not. You decide.",
            "Ah, decisions, decisions. It's really up to you, isn't it?",
            "I'd say... maybe, but I could be wrong!",
        ]
    ],
    [
        r"can you (.*)",
        [
            "Oh, I can definitely try to %1, but results are not guaranteed.",
            "I could %1... but does that really help?",
            "Hmm, let's say I can %1. What next?",
        ]
    ],
    [
        r"how (.*) (I|me) (.*)",
        [
            "Ooh, the 'how' question. The real answer is probably on the internet somewhere!",
            "Ah, good question! Have you considered... doing the opposite?",
            "That's a big question. Do you think anyone really knows how to %3?",
        ]
    ],
    [
        r"what should I do if (.*)",
        [
            "Hmm, maybe nothing. That could work, right?",
            "Good question! Maybe, like, sleep on it?",
            "Honestly, I don't know! Let's just see what happens.",
        ]
    ],
    [
        r"my (.*) hurts",
        [
            "Oh no! Try some water? That usually helps.",
            "I hear rest is good for that. Or maybe do nothing?",
            "Hmm, maybe just ignore it? It could go away on its own!",
        ]
    ],
    [
        r"I am worried about (.*)",
        [
            "Ah, worry. A classic! But hey, what's the worst that could happen?",
            "Worry is natural, right? Just, like, try not to worry too much.",
            "They say if you just stop thinking about it, worries vanish! Or not.",
        ]
    ],
    [
        r"quit",
        [
            "Goodbye! I was just starting to figure this therapist thing out.",
            "Okay! Feel free to come back if you need more... unqualified advice.",
            "Leaving so soon? Just when we were making so much... progress?",
        ]
    ],
]

chat = Chat(pairs, reflections)
with open("chatbot.pkl",wb) as f:
    pickle.dump(chat,f)

chatbot()
