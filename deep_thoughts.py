"""Random deep thought generator inspired by absurd one-liners and dad-joke monologues."""

from __future__ import annotations

import random

OPENERS = [
    "If",
    "Sometimes I wonder if",
    "You ever notice how",
    "I realized that if",
    "What if",
    "Nobody talks about how",
    "I keep thinking that if",
    "Late at night I suspect",
    "Imagine if",
    "In a perfect world,",
]

SUBJECTS = [
    "a coffee mug",
    "my alarm clock",
    "a lawn chair",
    "the office printer",
    "a sandwich",
    "my left sock",
    "a shopping cart",
    "the moon",
    "a staircase",
    "my calendar",
    "a traffic cone",
    "my houseplant",
]

ACTIONS = [
    "ran a startup",
    "wrote a self-help book",
    "became a life coach",
    "hosted a podcast",
    "started giving legal advice",
    "applied for management",
    "tried online dating",
    "joined a marching band",
    "filed taxes",
    "took improv classes",
]

TWISTS = [
    "it would still ghost me on Monday mornings",
    "we'd all pretend to understand it in meetings",
    "somebody would ask it to fix the Wi-Fi",
    "it would demand a standing desk and never stand",
    "it would schedule a brainstorm and bring no ideas",
    "it would call itself minimalist while owning six hats",
    "it would blame Mercury retrograde for every typo",
    "nobody would question it until performance review season",
    "it would somehow become my emergency contact",
    "it would ask for oat milk and then drink water",
]

CLOSERS = [
    "and that's probably why Tuesdays feel personal.",
    "which explains at least half of adulthood.",
    "and honestly, that feels emotionally accurate.",
    "which is either wisdom or a sleep deficit.",
    "and that's the kind of leadership nobody asked for.",
    "which is funny until your group chat agrees.",
    "and now I can't unthink it.",
    "which is why I don't trust motivational posters.",
    "and somehow that still makes more sense than airline boarding.",
    "which proves the universe loves a punchline.",
]


def get_total_possible_thoughts() -> int:
    """Return the total number of unique thoughts this generator can produce."""

    return len(OPENERS) * len(SUBJECTS) * len(ACTIONS) * len(TWISTS) * len(CLOSERS)


def get_random_thought() -> str:
    """Return one random deep-thought-style monologue line."""

    return " ".join(
        [
            random.choice(OPENERS),
            random.choice(SUBJECTS),
            random.choice(ACTIONS) + ",",
            random.choice(TWISTS),
            random.choice(CLOSERS),
        ]
    )
