"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#DirectoryUnavailableReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_directory_service_data.errors import DeserializationError

DirectoryUnavailableReason: TypeAlias = Literal[
    "INVALID_DIRECTORY_STATE",
    "DIRECTORY_TIMEOUT",
    "DIRECTORY_RESOURCES_EXCEEDED",
    "NO_DISK_SPACE",
    "TRUST_AUTH_FAILURE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INVALID_DIRECTORY_STATE",
        "DIRECTORY_TIMEOUT",
        "DIRECTORY_RESOURCES_EXCEEDED",
        "NO_DISK_SPACE",
        "TRUST_AUTH_FAILURE",
    )
)


def serialize_json(value: DirectoryUnavailableReason) -> str:
    return value


def deserialize_json(data: str) -> DirectoryUnavailableReason:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DirectoryUnavailableReason value: {data!r}"
        )
    return cast(DirectoryUnavailableReason, data)
