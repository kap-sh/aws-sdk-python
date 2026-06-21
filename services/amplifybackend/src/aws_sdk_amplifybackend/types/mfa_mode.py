"""Generated from Smithy shape ``com.amazonaws.amplifybackend#MFAMode``."""

from typing import Literal, TypeAlias, cast

MFAMode: TypeAlias = Literal[
    "ON",
    "OFF",
    "OPTIONAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: MFAMode) -> str:
    return value


def deserialize_json(data: str) -> MFAMode:
    return cast(MFAMode, data)
