"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ResultRows``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.result_field

ResultRows: TypeAlias = list["aws_sdk_cloudwatch_logs.types.result_field.ResultField"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResultRows) -> list:
    import aws_sdk_cloudwatch_logs.types.result_field

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch_logs.types.result_field.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ResultRows:
    import aws_sdk_cloudwatch_logs.types.result_field

    out: ResultRows = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch_logs.types.result_field.deserialize_aws_json_1_1(item)
        )
    return out
