"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#DirectoryRegistrationStatus``."""

from typing import Literal, TypeAlias, cast

DirectoryRegistrationStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "DELETING",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DirectoryRegistrationStatus) -> str:
    return value


def deserialize_json(data: str) -> DirectoryRegistrationStatus:
    return cast(DirectoryRegistrationStatus, data)
