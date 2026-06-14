"""Generated from Smithy shape ``com.amazonaws.datazone#ProjectStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

ProjectStatus: TypeAlias = Literal[
    "ACTIVE",
    "DELETING",
    "DELETE_FAILED",
    "UPDATING",
    "UPDATE_FAILED",
    "MOVING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "DELETING",
        "DELETE_FAILED",
        "UPDATING",
        "UPDATE_FAILED",
        "MOVING",
    )
)


def serialize_json(value: ProjectStatus) -> str:
    return value


def deserialize_json(data: str) -> ProjectStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProjectStatus value: {data!r}")
    return cast(ProjectStatus, data)
