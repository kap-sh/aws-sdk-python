"""Generated from Smithy shape ``com.amazonaws.workdocs#ResourceStateType``."""

from typing import Literal, TypeAlias, cast

ResourceStateType: TypeAlias = Literal[
    "ACTIVE",
    "RESTORING",
    "RECYCLING",
    "RECYCLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceStateType) -> str:
    return value


def deserialize_json(data: str) -> ResourceStateType:
    return cast(ResourceStateType, data)
