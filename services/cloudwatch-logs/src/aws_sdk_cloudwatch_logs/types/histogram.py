"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#Histogram``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.time
    import aws_sdk_cloudwatch_logs.types.count

Histogram: TypeAlias = dict[
    "aws_sdk_cloudwatch_logs.types.time.Time",
    "aws_sdk_cloudwatch_logs.types.count.Count",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: Histogram) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> Histogram:
    out: Histogram = {}
    for key, value in data.items():
        out[key] = value
    return out
