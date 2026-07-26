"""Generated from Smithy shape ``com.amazonaws.qbusiness#ScoreConfidence``."""

from typing import Literal, TypeAlias, cast

ScoreConfidence: TypeAlias = Literal[
    "VERY_HIGH",
    "HIGH",
    "MEDIUM",
    "LOW",
    "NOT_AVAILABLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScoreConfidence) -> str:
    return value


def deserialize_json(data: str) -> ScoreConfidence:
    return cast(ScoreConfidence, data)
