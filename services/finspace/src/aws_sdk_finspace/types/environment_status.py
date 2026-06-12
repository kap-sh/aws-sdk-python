"""Generated from Smithy shape ``com.amazonaws.finspace#EnvironmentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_finspace.errors import DeserializationError

EnvironmentStatus: TypeAlias = Literal[
    "CREATE_REQUESTED",
    "CREATING",
    "CREATED",
    "DELETE_REQUESTED",
    "DELETING",
    "DELETED",
    "FAILED_CREATION",
    "RETRY_DELETION",
    "FAILED_DELETION",
    "UPDATE_NETWORK_REQUESTED",
    "UPDATING_NETWORK",
    "FAILED_UPDATING_NETWORK",
    "SUSPENDED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE_REQUESTED",
        "CREATING",
        "CREATED",
        "DELETE_REQUESTED",
        "DELETING",
        "DELETED",
        "FAILED_CREATION",
        "RETRY_DELETION",
        "FAILED_DELETION",
        "UPDATE_NETWORK_REQUESTED",
        "UPDATING_NETWORK",
        "FAILED_UPDATING_NETWORK",
        "SUSPENDED",
    )
)


def serialize_json(value: EnvironmentStatus) -> str:
    return value


def deserialize_json(data: str) -> EnvironmentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EnvironmentStatus value: {data!r}")
    return cast(EnvironmentStatus, data)
