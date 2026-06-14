"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ScheduledQueryDestinationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch_logs.errors import DeserializationError

ScheduledQueryDestinationType: TypeAlias = Literal["S3",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("S3",))


def serialize_aws_json_1_1(value: ScheduledQueryDestinationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScheduledQueryDestinationType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ScheduledQueryDestinationType value: {data!r}"
        )
    return cast(ScheduledQueryDestinationType, data)
