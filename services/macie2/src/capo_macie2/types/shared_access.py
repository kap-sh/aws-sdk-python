"""Generated from Smithy shape ``com.amazonaws.macie2#SharedAccess``."""

from typing import Literal, TypeAlias, cast

SharedAccess: TypeAlias = Literal[
    "EXTERNAL",
    "INTERNAL",
    "NOT_SHARED",
    "UNKNOWN",
]


# --- restJson1 ser/de ---
def serialize_json(value: SharedAccess) -> str:
    return value


def deserialize_json(data: str) -> SharedAccess:
    return cast(SharedAccess, data)
