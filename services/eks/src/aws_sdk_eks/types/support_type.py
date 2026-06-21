"""Generated from Smithy shape ``com.amazonaws.eks#SupportType``."""

from typing import Literal, TypeAlias, cast

SupportType: TypeAlias = Literal[
    "STANDARD",
    "EXTENDED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SupportType) -> str:
    return value


def deserialize_json(data: str) -> SupportType:
    return cast(SupportType, data)
