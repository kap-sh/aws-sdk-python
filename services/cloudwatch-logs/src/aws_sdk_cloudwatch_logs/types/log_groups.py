"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#LogGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.log_group

LogGroups: TypeAlias = list["aws_sdk_cloudwatch_logs.types.log_group.LogGroup"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogGroups) -> list:
    import aws_sdk_cloudwatch_logs.types.log_group

    out: list = []
    for item in value:
        out.append(aws_sdk_cloudwatch_logs.types.log_group.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LogGroups:
    import aws_sdk_cloudwatch_logs.types.log_group

    out: LogGroups = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch_logs.types.log_group.deserialize_aws_json_1_1(item)
        )
    return out
