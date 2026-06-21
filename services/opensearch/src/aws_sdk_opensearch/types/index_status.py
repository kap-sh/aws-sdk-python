"""Generated from Smithy shape ``com.amazonaws.opensearch#IndexStatus``."""

from typing import Literal, TypeAlias, cast

IndexStatus: TypeAlias = Literal[
    "CREATED",
    "UPDATED",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: IndexStatus) -> str:
    return value


def deserialize_json(data: str) -> IndexStatus:
    return cast(IndexStatus, data)
