"""Generated from Smithy shape ``com.amazonaws.qbusiness#MessageUsefulnessReason``."""

from typing import Literal, TypeAlias, cast

MessageUsefulnessReason: TypeAlias = Literal[
    "NOT_FACTUALLY_CORRECT",
    "HARMFUL_OR_UNSAFE",
    "INCORRECT_OR_MISSING_SOURCES",
    "NOT_HELPFUL",
    "FACTUALLY_CORRECT",
    "COMPLETE",
    "RELEVANT_SOURCES",
    "HELPFUL",
    "NOT_BASED_ON_DOCUMENTS",
    "NOT_COMPLETE",
    "NOT_CONCISE",
    "OTHER",
]


# --- restJson1 ser/de ---
def serialize_json(value: MessageUsefulnessReason) -> str:
    return value


def deserialize_json(data: str) -> MessageUsefulnessReason:
    return cast(MessageUsefulnessReason, data)
