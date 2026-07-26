"""Generated from Smithy shape ``com.amazonaws.workdocs#BooleanEnumType``."""

from typing import Literal, TypeAlias, cast

BooleanEnumType: TypeAlias = Literal[
    "TRUE",
    "FALSE",
]


# --- restJson1 ser/de ---
def serialize_json(value: BooleanEnumType) -> str:
    return value


def deserialize_json(data: str) -> BooleanEnumType:
    return cast(BooleanEnumType, data)
