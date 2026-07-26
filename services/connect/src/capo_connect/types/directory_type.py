"""Generated from Smithy shape ``com.amazonaws.connect#DirectoryType``."""

from typing import Literal, TypeAlias, cast

DirectoryType: TypeAlias = Literal[
    "SAML",
    "CONNECT_MANAGED",
    "EXISTING_DIRECTORY",
]


# --- restJson1 ser/de ---
def serialize_json(value: DirectoryType) -> str:
    return value


def deserialize_json(data: str) -> DirectoryType:
    return cast(DirectoryType, data)
