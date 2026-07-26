"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#DirectoryRegistrationStatusReason``."""

from typing import Literal, TypeAlias, cast

DirectoryRegistrationStatusReason: TypeAlias = Literal[
    "DIRECTORY_ACCESS_DENIED",
    "DIRECTORY_RESOURCE_NOT_FOUND",
    "DIRECTORY_NOT_ACTIVE",
    "DIRECTORY_NOT_REACHABLE",
    "DIRECTORY_TYPE_NOT_SUPPORTED",
    "INTERNAL_FAILURE",
]


# --- restJson1 ser/de ---
def serialize_json(value: DirectoryRegistrationStatusReason) -> str:
    return value


def deserialize_json(data: str) -> DirectoryRegistrationStatusReason:
    return cast(DirectoryRegistrationStatusReason, data)
