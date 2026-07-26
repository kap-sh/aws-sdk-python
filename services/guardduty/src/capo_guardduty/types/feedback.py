"""Generated from Smithy shape ``com.amazonaws.guardduty#Feedback``."""

from typing import Literal, TypeAlias, cast

Feedback: TypeAlias = Literal[
    "USEFUL",
    "NOT_USEFUL",
]


# --- restJson1 ser/de ---
def serialize_json(value: Feedback) -> str:
    return value


def deserialize_json(data: str) -> Feedback:
    return cast(Feedback, data)
