"""Generated from Smithy shape ``com.amazonaws.datazone#UserAssignment``."""

from typing import Literal, TypeAlias, cast

UserAssignment: TypeAlias = Literal[
    "AUTOMATIC",
    "MANUAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: UserAssignment) -> str:
    return value


def deserialize_json(data: str) -> UserAssignment:
    return cast(UserAssignment, data)
