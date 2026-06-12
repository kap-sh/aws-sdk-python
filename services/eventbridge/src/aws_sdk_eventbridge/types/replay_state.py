"""Generated from Smithy shape ``com.amazonaws.eventbridge#ReplayState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_eventbridge.errors import DeserializationError

ReplayState: TypeAlias = Literal[
    "STARTING",
    "RUNNING",
    "CANCELLING",
    "COMPLETED",
    "CANCELLED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STARTING",
        "RUNNING",
        "CANCELLING",
        "COMPLETED",
        "CANCELLED",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: ReplayState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReplayState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReplayState value: {data!r}")
    return cast(ReplayState, data)
