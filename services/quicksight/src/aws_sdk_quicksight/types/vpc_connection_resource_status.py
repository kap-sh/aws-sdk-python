"""Generated from Smithy shape ``com.amazonaws.quicksight#VPCConnectionResourceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

VPCConnectionResourceStatus: TypeAlias = Literal[
    "CREATION_IN_PROGRESS",
    "CREATION_SUCCESSFUL",
    "CREATION_FAILED",
    "UPDATE_IN_PROGRESS",
    "UPDATE_SUCCESSFUL",
    "UPDATE_FAILED",
    "DELETION_IN_PROGRESS",
    "DELETION_FAILED",
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
        "DELETION_IN_PROGRESS",
        "DELETION_FAILED",
        "DELETED",
    )
)


def serialize_json(value: VPCConnectionResourceStatus) -> str:
    return value


def deserialize_json(data: str) -> VPCConnectionResourceStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown VPCConnectionResourceStatus value: {data!r}"
        )
    return cast(VPCConnectionResourceStatus, data)
