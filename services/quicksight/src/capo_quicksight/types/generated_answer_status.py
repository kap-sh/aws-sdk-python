"""Generated from Smithy shape ``com.amazonaws.quicksight#GeneratedAnswerStatus``."""

from typing import Literal, TypeAlias, cast

GeneratedAnswerStatus: TypeAlias = Literal[
    "ANSWER_GENERATED",
    "ANSWER_RETRIEVED",
    "ANSWER_DOWNGRADE",
]


# --- restJson1 ser/de ---
def serialize_json(value: GeneratedAnswerStatus) -> str:
    return value


def deserialize_json(data: str) -> GeneratedAnswerStatus:
    return cast(GeneratedAnswerStatus, data)
