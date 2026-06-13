"""Generated from Smithy shape ``com.amazonaws.quicksight#NetworkInterfaceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

NetworkInterfaceStatus: TypeAlias = Literal[
    "CREATING",
    "AVAILABLE",
    "CREATION_FAILED",
    "UPDATING",
    "UPDATE_FAILED",
    "DELETING",
    "DELETED",
    "DELETION_FAILED",
    "DELETION_SCHEDULED",
    "ATTACHMENT_FAILED_ROLLBACK_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "AVAILABLE",
        "CREATION_FAILED",
        "UPDATING",
        "UPDATE_FAILED",
        "DELETING",
        "DELETED",
        "DELETION_FAILED",
        "DELETION_SCHEDULED",
        "ATTACHMENT_FAILED_ROLLBACK_FAILED",
    )
)


def serialize_json(value: NetworkInterfaceStatus) -> str:
    return value


def deserialize_json(data: str) -> NetworkInterfaceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NetworkInterfaceStatus value: {data!r}")
    return cast(NetworkInterfaceStatus, data)
