"""Generated from Smithy shape ``com.amazonaws.finspace#KxVolumeStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_finspace.errors import DeserializationError

KxVolumeStatus: TypeAlias = Literal[
    "CREATING",
    "CREATE_FAILED",
    "ACTIVE",
    "UPDATING",
    "UPDATED",
    "UPDATE_FAILED",
    "DELETING",
    "DELETED",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "CREATE_FAILED",
        "ACTIVE",
        "UPDATING",
        "UPDATED",
        "UPDATE_FAILED",
        "DELETING",
        "DELETED",
        "DELETE_FAILED",
    )
)


def serialize_json(value: KxVolumeStatus) -> str:
    return value


def deserialize_json(data: str) -> KxVolumeStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KxVolumeStatus value: {data!r}")
    return cast(KxVolumeStatus, data)
