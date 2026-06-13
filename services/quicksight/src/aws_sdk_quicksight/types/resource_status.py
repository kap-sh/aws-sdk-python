"""Generated from Smithy shape ``com.amazonaws.quicksight#ResourceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

ResourceStatus: TypeAlias = Literal[
    "CREATION_IN_PROGRESS",
    "CREATION_SUCCESSFUL",
    "CREATION_FAILED",
    "UPDATE_IN_PROGRESS",
    "UPDATE_SUCCESSFUL",
    "UPDATE_FAILED",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATION_IN_PROGRESS",
        "CREATION_SUCCESSFUL",
        "CREATION_FAILED",
        "UPDATE_IN_PROGRESS",
        "UPDATE_SUCCESSFUL",
        "UPDATE_FAILED",
        "DELETED",
    )
)


def serialize_json(value: ResourceStatus) -> str:
    return value


def deserialize_json(data: str) -> ResourceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceStatus value: {data!r}")
    return cast(ResourceStatus, data)
