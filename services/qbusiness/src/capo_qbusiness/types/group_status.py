"""Generated from Smithy shape ``com.amazonaws.qbusiness#GroupStatus``."""

from typing import Literal, TypeAlias, cast

GroupStatus: TypeAlias = Literal[
    "FAILED",
    "SUCCEEDED",
    "PROCESSING",
    "DELETING",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupStatus) -> str:
    return value


def deserialize_json(data: str) -> GroupStatus:
    return cast(GroupStatus, data)
