"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#LogGroupNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.log_group_name

LogGroupNames: TypeAlias = list[
    "aws_sdk_cloudwatch_logs.types.log_group_name.LogGroupName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogGroupNames) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> LogGroupNames:
    return list(data)
