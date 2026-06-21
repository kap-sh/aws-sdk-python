"""Generated from Smithy shape ``com.amazonaws.connect#LexVersion``."""

from typing import Literal, TypeAlias, cast

LexVersion: TypeAlias = Literal[
    "V1",
    "V2",
]


# --- restJson1 ser/de ---
def serialize_json(value: LexVersion) -> str:
    return value


def deserialize_json(data: str) -> LexVersion:
    return cast(LexVersion, data)
