"""Generated from Smithy shape ``com.amazonaws.quicksight#IncludeGeneratedAnswer``."""

from typing import Literal, TypeAlias, cast

IncludeGeneratedAnswer: TypeAlias = Literal[
    "INCLUDE",
    "EXCLUDE",
]


# --- restJson1 ser/de ---
def serialize_json(value: IncludeGeneratedAnswer) -> str:
    return value


def deserialize_json(data: str) -> IncludeGeneratedAnswer:
    return cast(IncludeGeneratedAnswer, data)
