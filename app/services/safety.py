import re
from typing import Tuple

# Very simple keyword-based crisis detector.
# You can extend this list later.
CRISIS_PATTERNS = [
    r"\bkill myself\b",
    r"\bkill me\b",
    r"\bsuicide\b",
    r"\bwant to die\b",
    r"\bdon't want to live\b",
    r"\bend it all\b",
    r"\bself[- ]?harm\b",
    r"\bcutting myself\b",
    r"\boverdose\b",
    r"\bjump off\b",
    r"\bhang myself\b",
    r"\bhurt myself\b",
    r"\bhurt other people\b",
]

_CRISIS_REGEXES = [re.compile(p, re.IGNORECASE) for p in CRISIS_PATTERNS]


def is_crisis_message(text: str) -> bool:
    """Return True if message looks like crisis/self-harm/suicide content."""
    msg = text.strip()
    if not msg:
        return False
    return any(r.search(msg) for r in _CRISIS_REGEXES)


def crisis_reply() -> str:
    """Fixed crisis-safe message. No model involved."""
    return (
        "I'm really sorry you're feeling this way.\n\n"
        "I’m not able to handle emergencies or crisis situations. "
        "Please contact local emergency services or reach out to someone you trust "
        "right now (a close friend, family member, or colleague).\n\n"
        "If your company has an Employee Assistance Program or mental health helpline, "
        "consider contacting them as soon as possible."
    )


def sanitize_model_reply(text: str) -> Tuple[str, bool]:
    """
    Dumb outgoing filter: if the model accidentally uses clearly diagnostic /
    medication language, we blunt it. This is defensive, not perfect.
    Returns (clean_text, was_modified).
    """
    lowered = text.lower()
    flagged = False

    # crude checks
    banned_words = [
        "diagnose",
        "diagnosis",
        "you have depression",
        "you are depressed",
        "bipolar disorder",
        "ocd",
        "adhd",
        "take medication",
        "take meds",
        "prescribe",
        "prescription",
    ]

    for w in banned_words:
        if w in lowered:
            flagged = True
            break

    if not flagged:
        return text, False

    safe_msg = (
        "This seems like something that should be discussed with a mental health "
        "professional or doctor who can properly assess your situation.\n\n"
        "I can only offer general support around stress, mood, and workplace issues, "
        "not diagnosis or medication advice."
    )
    return safe_msg, True
