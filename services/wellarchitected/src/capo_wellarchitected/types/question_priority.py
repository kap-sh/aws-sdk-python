"""Generated from Smithy shape ``com.amazonaws.wellarchitected#QuestionPriority``."""

from typing import Literal, TypeAlias, cast

QuestionPriority: TypeAlias = Literal[
    "PRIORITIZED",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: QuestionPriority) -> str:
    return value


def deserialize_json(data: str) -> QuestionPriority:
    return cast(QuestionPriority, data)
