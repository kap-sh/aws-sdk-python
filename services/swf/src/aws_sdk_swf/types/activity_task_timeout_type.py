"""Generated from Smithy shape ``com.amazonaws.swf#ActivityTaskTimeoutType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_swf.errors import DeserializationError

ActivityTaskTimeoutType: TypeAlias = Literal[
    "START_TO_CLOSE",
    "SCHEDULE_TO_START",
    "SCHEDULE_TO_CLOSE",
    "HEARTBEAT",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "START_TO_CLOSE",
        "SCHEDULE_TO_START",
        "SCHEDULE_TO_CLOSE",
        "HEARTBEAT",
    )
)


def serialize_aws_json_1_0(value: ActivityTaskTimeoutType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ActivityTaskTimeoutType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActivityTaskTimeoutType value: {data!r}")
    return cast(ActivityTaskTimeoutType, data)
