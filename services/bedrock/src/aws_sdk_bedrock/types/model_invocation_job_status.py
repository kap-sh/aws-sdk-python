"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelInvocationJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

ModelInvocationJobStatus: TypeAlias = Literal[
    "Submitted",
    "InProgress",
    "Completed",
    "Failed",
    "Stopping",
    "Stopped",
    "PartiallyCompleted",
    "Expired",
    "Validating",
    "Scheduled",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Submitted",
        "InProgress",
        "Completed",
        "Failed",
        "Stopping",
        "Stopped",
        "PartiallyCompleted",
        "Expired",
        "Validating",
        "Scheduled",
    )
)


def serialize_json(value: ModelInvocationJobStatus) -> str:
    return value


def deserialize_json(data: str) -> ModelInvocationJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelInvocationJobStatus value: {data!r}")
    return cast(ModelInvocationJobStatus, data)
