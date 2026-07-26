"""Generated from Smithy shape ``com.amazonaws.iot#IndexStatus``."""

from typing import Literal, TypeAlias, cast

IndexStatus: TypeAlias = Literal[
    "ACTIVE",
    "BUILDING",
    "REBUILDING",
]


# --- restJson1 ser/de ---
def serialize_json(value: IndexStatus) -> str:
    return value


def deserialize_json(data: str) -> IndexStatus:
    return cast(IndexStatus, data)
