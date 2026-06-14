"""Generated from Smithy shape ``com.amazonaws.datazone#EnvironmentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

EnvironmentStatus: TypeAlias = Literal[
    "ACTIVE",
    "CREATING",
    "UPDATING",
    "DELETING",
    "CREATE_FAILED",
    "UPDATE_FAILED",
    "DELETE_FAILED",
    "VALIDATION_FAILED",
    "SUSPENDED",
    "DISABLED",
    "EXPIRED",
    "DELETED",
    "INACCESSIBLE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "CREATING",
        "UPDATING",
        "DELETING",
        "CREATE_FAILED",
        "UPDATE_FAILED",
        "DELETE_FAILED",
        "VALIDATION_FAILED",
        "SUSPENDED",
        "DISABLED",
        "EXPIRED",
        "DELETED",
        "INACCESSIBLE",
    )
)


def serialize_json(value: EnvironmentStatus) -> str:
    return value


def deserialize_json(data: str) -> EnvironmentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EnvironmentStatus value: {data!r}")
    return cast(EnvironmentStatus, data)
