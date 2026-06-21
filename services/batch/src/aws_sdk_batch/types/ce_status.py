"""Generated from Smithy shape ``com.amazonaws.batch#CEStatus``."""

from typing import Literal, TypeAlias, cast

CEStatus: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "DELETING",
    "DELETED",
    "VALID",
    "INVALID",
]


# --- restJson1 ser/de ---
def serialize_json(value: CEStatus) -> str:
    return value


def deserialize_json(data: str) -> CEStatus:
    return cast(CEStatus, data)
