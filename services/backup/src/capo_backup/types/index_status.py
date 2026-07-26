"""Generated from Smithy shape ``com.amazonaws.backup#IndexStatus``."""

from typing import Literal, TypeAlias, cast

IndexStatus: TypeAlias = Literal[
    "PENDING",
    "ACTIVE",
    "FAILED",
    "DELETING",
]


# --- restJson1 ser/de ---
def serialize_json(value: IndexStatus) -> str:
    return value


def deserialize_json(data: str) -> IndexStatus:
    return cast(IndexStatus, data)
