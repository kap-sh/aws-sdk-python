"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ActionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch_logs.errors import DeserializationError

ActionStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "CLIENT_ERROR",
    "FAILED",
    "COMPLETE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "CLIENT_ERROR",
        "FAILED",
        "COMPLETE",
    )
)


def serialize_aws_json_1_1(value: ActionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ActionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActionStatus value: {data!r}")
    return cast(ActionStatus, data)
