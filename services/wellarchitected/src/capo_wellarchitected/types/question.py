"""Generated from Smithy shape ``com.amazonaws.wellarchitected#Question``."""

from typing import Literal, TypeAlias, cast

Question: TypeAlias = Literal[
    "UNANSWERED",
    "ANSWERED",
]


# --- restJson1 ser/de ---
def serialize_json(value: Question) -> str:
    return value


def deserialize_json(data: str) -> Question:
    return cast(Question, data)
