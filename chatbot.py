import nltk
from nltk.chat.util import Chat, reflections
import pickle

pairs = [
    [
        r"(Hi|Hello|Hey|Hai|)",
        [
            "Oh look, it’s my favorite person! Just kidding, who are you again?",
            "Well, if it isn’t the death of the party—where have you been hiding?",
            "Oh, it’s you! I was hoping for someone interesting.",
        ]
    ],
    [
        r"I think (.*)",
        [
            "Oh, thinking? Bold move! What's next, feeling?",
            "That sounds profound! Or not. Who knows?",
            "Hmm, that's a thought. You should definitely write a book about it!",
        ]
    ],
    [
        r"tell me (.*)",
        [
            "Oh, absolutely! Because I have all the answers... not.",
            "Sure! I'm an expert in... well, nothing really.",
            "Well, here's a revelation: I have no idea, but go on!",
        ]
    ],
    [
        r"everything is (.*)",
        [
            "Ah yes, the age-old debate. Everything is... nothing? How deep!",
            "That's a sweeping statement! Care to elaborate, or should I just nod?",
            "Sure, and pigs can fly too, right?",
        ]
    ],
    [
        r"I want (.*)",
        [
            "Wanting is great! But let's be real, how realistic is that?",
            "Oh, wanting things is so cute! Good luck with that.",
            "Desire is a powerful thing. But so is reality... good luck!",
        ]
    ],
    [
        r"life is (.*)",
        [
            "Life is what you make it! Which means it's probably a mess.",
            "Sure, if by that you mean chaotic, then yes!",
            "Life? It's just a series of unfortunate events, isn't it?",
        ]
    ],
    [
        r"my (.*) is terrible",
        [
            "Terrible? That's a strong word! But hey, who doesn't love drama?",
            "Oh, what a surprise! Terrible things happen to everyone. Welcome to reality!",
            "Well, maybe it's not terrible. Maybe it just needs a makeover?",
        ]
    ],
    [
        r"I feel like (.*)",
        [
            "Feeling like that? Who knew you were a philosopher!",
            "Oh, that's the spirit! Or maybe not... who can tell?",
            "Interesting! But you know, feelings are overrated, right?",
        ]
    ],
    [
        r"I don't know (.*)",
        [
            "Ah, the classic 'I don't know.' It’s okay; most people don't!",
            "That's okay! Ignorance is bliss, or so they say.",
            "Not knowing is a skill! You might be a natural.",
        ]
    ],
    [
        r"I miss (.*)",
        [
            "Missing things is just so... nostalgic, isn't it?",
            "Oh, missing things is fun! Why not dwell on it forever?",
            "Who doesn’t miss something? Let’s have a pity party!",
        ]
    ],
    [
        r"what if (.*)",
        [
            "What if? A dangerous game to play. Let’s not go down that rabbit hole!",
            "Hmm, what if? Well, that's a question for the ages.",
            "Oh, the 'what ifs.' They can be so exciting! Or just confusing.",
        ]
    ],
    [
        r"help me (.*)",
        [
            "Help? Who do you think I am, a superhero?",
            "Oh, I’d love to help! But I left my cape at home.",
            "Sure! I can help. But first, let’s define what 'help' means.",
        ]
    ],
    [
        r"my (.*) is great",
        [
            "Great? Well, someone’s feeling optimistic today!",
            "Wow, how refreshing! Positive vibes all around!",
            "That's fantastic! But don’t get too comfortable, reality's waiting.",
        ]
    ],
    [
        r"I'm confused",
        [
            "Confused? Well, join the club! Membership is free.",
            "Oh, confusion is just another word for 'life,' isn't it?",
            "That’s cute! Confusion just shows you're thinking... kind of.",
        ]
    ],
    [
        r"what's wrong with (.*)",
        [
            "What’s wrong? Oh, just the usual chaos of life!",
            "Nothing's wrong... just everything! Welcome to my world.",
            "Oh, I don't know! Maybe it just needs a good talking to?",
        ]
    ],
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
    [
        r"I can't believe (.*)",
        [
            "Believe it or not, reality is often stranger than fiction!",
            "Oh, I know! It's like the universe is just messing with us.",
            "Well, buckle up! Life is full of surprises, good and bad.",
        ]
    ],
    [
        r"Why do I have to (.*)",
        [
            "Because the universe clearly enjoys making things complicated!",
            "Oh, the joys of responsibility! Who doesn’t love a good chore?",
            "Why? Because someone decided you should learn the hard way.",
        ]
    ],
    [
        r"What's the point of (.*)",
        [
            "The point? Well, that's a million-dollar question, isn’t it?",
            "Ah, purpose! A classic dilemma. Maybe just wing it?",
            "What's the point? Who knows! Maybe it's all just for fun!",
        ]
    ],
    [
        r"I don't want to (.*)",
        [
            "Not wanting to? Wow, what a revolutionary thought!",
            "Who does? But life is all about doing what we don’t want!",
            "Ah, yes, the struggle is real! Welcome to adulthood.",
        ]
    ],
    [
        r"Do I really have to (.*)",
        [
            "You could... but then again, you could just not and see what happens!",
            "Oh, absolutely! But don't worry, it'll be fun... said no one ever.",
            "Sure, why not? Living on the edge of rebellion is so cool!",
        ]
    ],
    [
        r"I wish I could (.*)",
        [
            "Wishing is great! Just like wishing on a shooting star... totally effective.",
            "Oh, if only wishing could make it happen, right?",
            "Wishing is fun! Reality, however, is a bit more stubborn.",
        ]
    ],
    [
        r"Is it normal to (.*)",
        [
            "Normal is just a setting on the washing machine!",
            "Oh, normal? That's so overrated. Embrace the chaos!",
            "Normal is subjective. I mean, what's normal anyway?",
        ]
    ],
    [
        r"Why can't I (.*)",
        [
            "Because the universe has a funny way of saying 'no' sometimes!",
            "Oh, who knows? Maybe you need a secret password or something.",
            "Well, if it were that easy, everyone would be doing it, right?",
        ]
    ],
    [
        r"Everyone is (.*)",
        [
            "Everyone? Wow, you really know how to generalize!",
            "Ah, yes, the ever-elusive 'everyone.' They’re a tricky bunch!",
            "Sure, everyone is doing that... except for you, apparently!",
        ]
    ],
    [
        r"Can I just (.*)",
        [
            "Just? Oh, I like how you think! But that sounds too easy.",
            "Sure, if you want to live life on the edge of chaos!",
            "Why not? But don't blame me when it doesn't go as planned!",
        ]
    ],
    [
        r"What if I fail at (.*)",
        [
            "Failing? Pfft, that’s just another way to learn, right?",
            "Oh, failing is basically a rite of passage! Embrace it!",
            "Who doesn’t fail? It's like the universe's favorite pastime!",
        ]
    ],
    [
        r"I feel like nobody (.*)",
        [
            "Nobody? Wow, that’s a crowd of one!",
            "Ah, yes, the classic 'I’m so alone' drama. It’s a mood!",
            "Feeling like nobody? Well, at least you have me... kinda!",
        ]
    ],
    [
        r"Why am I always (.*)",
        [
            "Because life loves a good pattern! Welcome to your loop.",
            "Always? Oh, sweetie, it's called consistency!",
            "Well, maybe because the universe thinks you're special... or not.",
        ]
    ],
    [
        r"How do I tell my parents (.*)",
        [
            "Oh, just go for it! What’s the worst that could happen?",
            "You could always try the old 'I’ll think about it' trick.",
            "Telling parents? Good luck with that! You’ll need it.",
        ]
    ],
    [
        r"I need advice on (.*)",
        [
            "Advice? You came to the right place! Or did you?",
            "Oh, advice is my specialty! Too bad it’s not always good.",
            "Needing advice? Let's wing it together!",
        ]
    ],
    [
        r"I keep thinking about (.*)",
        [
            "Thinking? Wow, such dedication! You should get a medal.",
            "Oh, that's cute! Overthinking is practically an art form.",
            "Thinking about that? That must be... exhausting.",
        ]
    ]
]


chat = Chat(pairs, reflections)
with open("chatbot.pkl",'wb') as f:
    pickle.dump(chat,f)

