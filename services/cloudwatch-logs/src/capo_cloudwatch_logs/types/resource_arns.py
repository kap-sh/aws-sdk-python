"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ResourceArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.arn

ResourceArns: TypeAlias = list["capo_cloudwatch_logs.types.arn.Arn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceArns) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ResourceArns:
    return list(data)
