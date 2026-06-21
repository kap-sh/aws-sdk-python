"""Generated from Smithy shape ``com.amazonaws.rdsdata#LongReturnType``."""

from typing import Literal, TypeAlias, cast

LongReturnType: TypeAlias = Literal[
    "STRING",
    "LONG",
]


# --- restJson1 ser/de ---
def serialize_json(value: LongReturnType) -> str:
    return value


def deserialize_json(data: str) -> LongReturnType:
    return cast(LongReturnType, data)
