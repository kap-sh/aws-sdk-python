"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ExtractedValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.token
    import aws_sdk_cloudwatch_logs.types.value

ExtractedValues: TypeAlias = dict[
    "aws_sdk_cloudwatch_logs.types.token.Token",
    "aws_sdk_cloudwatch_logs.types.value.Value",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ExtractedValues) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> ExtractedValues:
    out: ExtractedValues = {}
    for key, value in data.items():
        out[key] = value
    return out
