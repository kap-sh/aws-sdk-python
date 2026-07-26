"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#DirectoryUnavailableReason``."""

from typing import Literal, TypeAlias, cast

DirectoryUnavailableReason: TypeAlias = Literal[
    "INVALID_DIRECTORY_STATE",
    "DIRECTORY_TIMEOUT",
    "DIRECTORY_RESOURCES_EXCEEDED",
    "NO_DISK_SPACE",
    "TRUST_AUTH_FAILURE",
]


# --- restJson1 ser/de ---
def serialize_json(value: DirectoryUnavailableReason) -> str:
    return value


def deserialize_json(data: str) -> DirectoryUnavailableReason:
    return cast(DirectoryUnavailableReason, data)
