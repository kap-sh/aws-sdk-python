"""Generated from Smithy shape ``com.amazonaws.devopsagent#Priority``."""

from typing import Literal, TypeAlias, cast

"""<p>Priority levels for tasks, from highest to lowest urgency</p>"""
Priority: TypeAlias = Literal[
    "CRITICAL",
    "HIGH",
    "MEDIUM",
    "LOW",
    "MINIMAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: Priority) -> str:
    return value


def deserialize_json(data: str) -> Priority:
    return cast(Priority, data)
