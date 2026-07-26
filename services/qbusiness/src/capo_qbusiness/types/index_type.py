"""Generated from Smithy shape ``com.amazonaws.qbusiness#IndexType``."""

from typing import Literal, TypeAlias, cast

IndexType: TypeAlias = Literal[
    "ENTERPRISE",
    "STARTER",
]


# --- restJson1 ser/de ---
def serialize_json(value: IndexType) -> str:
    return value


def deserialize_json(data: str) -> IndexType:
    return cast(IndexType, data)
