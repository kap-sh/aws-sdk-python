"""Generated from Smithy shape ``com.amazonaws.qbusiness#IndexStatus``."""

from typing import Literal, TypeAlias, cast

IndexStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "DELETING",
    "FAILED",
    "UPDATING",
]


# --- restJson1 ser/de ---
def serialize_json(value: IndexStatus) -> str:
    return value


def deserialize_json(data: str) -> IndexStatus:
    return cast(IndexStatus, data)
