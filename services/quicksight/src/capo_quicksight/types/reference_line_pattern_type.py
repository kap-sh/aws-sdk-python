"""Generated from Smithy shape ``com.amazonaws.quicksight#ReferenceLinePatternType``."""

from typing import Literal, TypeAlias, cast

ReferenceLinePatternType: TypeAlias = Literal[
    "SOLID",
    "DASHED",
    "DOTTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReferenceLinePatternType) -> str:
    return value


def deserialize_json(data: str) -> ReferenceLinePatternType:
    return cast(ReferenceLinePatternType, data)
