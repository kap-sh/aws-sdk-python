"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#Processors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.processor

Processors: TypeAlias = list["capo_cloudwatch_logs.types.processor.Processor"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Processors) -> list:
    import capo_cloudwatch_logs.types.processor

    out: list = []
    for item in value:
        out.append(capo_cloudwatch_logs.types.processor.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Processors:
    import capo_cloudwatch_logs.types.processor

    out: Processors = []
    for item in data:
        out.append(capo_cloudwatch_logs.types.processor.deserialize_aws_json_1_1(item))
    return out
