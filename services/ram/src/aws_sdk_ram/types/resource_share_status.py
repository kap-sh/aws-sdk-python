"""Generated from Smithy shape ``com.amazonaws.ram#ResourceShareStatus``."""

from typing import Literal, TypeAlias, cast

ResourceShareStatus: TypeAlias = Literal[
    "PENDING",
    "ACTIVE",
    "FAILED",
    "DELETING",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceShareStatus) -> str:
    return value


def deserialize_json(data: str) -> ResourceShareStatus:
    return cast(ResourceShareStatus, data)
