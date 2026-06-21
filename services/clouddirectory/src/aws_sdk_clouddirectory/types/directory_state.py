"""Generated from Smithy shape ``com.amazonaws.clouddirectory#DirectoryState``."""

from typing import Literal, TypeAlias, cast

DirectoryState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DirectoryState) -> str:
    return value


def deserialize_json(data: str) -> DirectoryState:
    return cast(DirectoryState, data)
