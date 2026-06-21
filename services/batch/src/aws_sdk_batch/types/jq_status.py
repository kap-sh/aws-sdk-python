"""Generated from Smithy shape ``com.amazonaws.batch#JQStatus``."""

from typing import Literal, TypeAlias, cast

JQStatus: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "DELETING",
    "DELETED",
    "VALID",
    "INVALID",
]


# --- restJson1 ser/de ---
def serialize_json(value: JQStatus) -> str:
    return value


def deserialize_json(data: str) -> JQStatus:
    return cast(JQStatus, data)
