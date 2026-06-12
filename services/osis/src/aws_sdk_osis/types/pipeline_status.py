"""Generated from Smithy shape ``com.amazonaws.osis#PipelineStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_osis.errors import DeserializationError

PipelineStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "DELETING",
    "CREATE_FAILED",
    "UPDATE_FAILED",
    "STARTING",
    "START_FAILED",
    "STOPPING",
    "STOPPED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "UPDATING",
        "DELETING",
        "CREATE_FAILED",
        "UPDATE_FAILED",
        "STARTING",
        "START_FAILED",
        "STOPPING",
        "STOPPED",
    )
)


def serialize_json(value: PipelineStatus) -> str:
    return value


def deserialize_json(data: str) -> PipelineStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PipelineStatus value: {data!r}")
    return cast(PipelineStatus, data)
