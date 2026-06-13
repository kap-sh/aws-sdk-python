"""Generated from Smithy shape ``com.amazonaws.bedrock#FineTuningJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

FineTuningJobStatus: TypeAlias = Literal[
    "InProgress",
    "Completed",
    "Failed",
    "Stopping",
    "Stopped",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InProgress",
        "Completed",
        "Failed",
        "Stopping",
        "Stopped",
    )
)


def serialize_json(value: FineTuningJobStatus) -> str:
    return value


def deserialize_json(data: str) -> FineTuningJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FineTuningJobStatus value: {data!r}")
    return cast(FineTuningJobStatus, data)
