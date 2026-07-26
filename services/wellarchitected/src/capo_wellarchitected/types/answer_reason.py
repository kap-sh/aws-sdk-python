"""Generated from Smithy shape ``com.amazonaws.wellarchitected#AnswerReason``."""

from typing import Literal, TypeAlias, cast

AnswerReason: TypeAlias = Literal[
    "OUT_OF_SCOPE",
    "BUSINESS_PRIORITIES",
    "ARCHITECTURE_CONSTRAINTS",
    "OTHER",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: AnswerReason) -> str:
    return value


def deserialize_json(data: str) -> AnswerReason:
    return cast(AnswerReason, data)
