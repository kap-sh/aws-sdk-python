"""Generated from Smithy shape ``com.amazonaws.wellarchitected#QuestionType``."""

from typing import Literal, TypeAlias, cast

QuestionType: TypeAlias = Literal[
    "PRIORITIZED",
    "NON_PRIORITIZED",
]


# --- restJson1 ser/de ---
def serialize_json(value: QuestionType) -> str:
    return value


def deserialize_json(data: str) -> QuestionType:
    return cast(QuestionType, data)
