"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#LogGroupArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.log_group_arn

LogGroupArnList: TypeAlias = list[
    "aws_sdk_cloudwatch_logs.types.log_group_arn.LogGroupArn"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogGroupArnList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> LogGroupArnList:
    return list(data)
