"""Generated from Smithy shape ``com.amazonaws.timestreamquery#ScheduledQueryRunStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_timestream_query.errors import DeserializationError

ScheduledQueryRunStatus: TypeAlias = Literal[
    "AUTO_TRIGGER_SUCCESS",
    "AUTO_TRIGGER_FAILURE",
    "MANUAL_TRIGGER_SUCCESS",
    "MANUAL_TRIGGER_FAILURE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTO_TRIGGER_SUCCESS",
        "AUTO_TRIGGER_FAILURE",
        "MANUAL_TRIGGER_SUCCESS",
        "MANUAL_TRIGGER_FAILURE",
    )
)


def serialize_aws_json_1_0(value: ScheduledQueryRunStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ScheduledQueryRunStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScheduledQueryRunStatus value: {data!r}")
    return cast(ScheduledQueryRunStatus, data)
