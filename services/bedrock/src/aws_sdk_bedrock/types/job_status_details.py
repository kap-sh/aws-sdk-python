"""Generated from Smithy shape ``com.amazonaws.bedrock#JobStatusDetails``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

JobStatusDetails: TypeAlias = Literal[
    "InProgress",
    "Completed",
    "Stopping",
    "Stopped",
    "Failed",
    "NotStarted",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InProgress",
        "Completed",
        "Stopping",
        "Stopped",
        "Failed",
        "NotStarted",
    )
)


def serialize_json(value: JobStatusDetails) -> str:
    return value


def deserialize_json(data: str) -> JobStatusDetails:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobStatusDetails value: {data!r}")
    return cast(JobStatusDetails, data)
