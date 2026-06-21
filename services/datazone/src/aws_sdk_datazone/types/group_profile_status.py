"""Generated from Smithy shape ``com.amazonaws.datazone#GroupProfileStatus``."""

from typing import Literal, TypeAlias, cast

GroupProfileStatus: TypeAlias = Literal[
    "ASSIGNED",
    "NOT_ASSIGNED",
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupProfileStatus) -> str:
    return value


def deserialize_json(data: str) -> GroupProfileStatus:
    return cast(GroupProfileStatus, data)
