"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ScheduledQueryDestinationType``."""

from typing import Literal, TypeAlias, cast

ScheduledQueryDestinationType: TypeAlias = Literal["S3",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScheduledQueryDestinationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScheduledQueryDestinationType:
    return cast(ScheduledQueryDestinationType, data)
