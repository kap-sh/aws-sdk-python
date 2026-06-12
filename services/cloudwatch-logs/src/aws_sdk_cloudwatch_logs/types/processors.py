"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#Processors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.processor

Processors: TypeAlias = list["aws_sdk_cloudwatch_logs.types.processor.Processor"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Processors) -> list:
    import aws_sdk_cloudwatch_logs.types.processor

    out: list = []
    for item in value:
        out.append(aws_sdk_cloudwatch_logs.types.processor.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Processors:
    import aws_sdk_cloudwatch_logs.types.processor

    out: Processors = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch_logs.types.processor.deserialize_aws_json_1_1(item)
        )
    return out
