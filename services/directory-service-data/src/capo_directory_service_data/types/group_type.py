"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#GroupType``."""

from typing import Literal, TypeAlias, cast

GroupType: TypeAlias = Literal[
    "Distribution",
    "Security",
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupType) -> str:
    return value


def deserialize_json(data: str) -> GroupType:
    return cast(GroupType, data)
