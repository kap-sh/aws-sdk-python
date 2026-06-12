"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#HeaderParametersMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.header_key
    import aws_sdk_cloudwatch_events.types.header_value

HeaderParametersMap: TypeAlias = dict[
    "aws_sdk_cloudwatch_events.types.header_key.HeaderKey",
    "aws_sdk_cloudwatch_events.types.header_value.HeaderValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: HeaderParametersMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> HeaderParametersMap:
    out: HeaderParametersMap = {}
    for key, value in data.items():
        out[key] = value
    return out
