"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#QueryStringParametersMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.query_string_key
    import aws_sdk_cloudwatch_events.types.query_string_value

QueryStringParametersMap: TypeAlias = dict[
    "aws_sdk_cloudwatch_events.types.query_string_key.QueryStringKey",
    "aws_sdk_cloudwatch_events.types.query_string_value.QueryStringValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: QueryStringParametersMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> QueryStringParametersMap:
    out: QueryStringParametersMap = {}
    for key, value in data.items():
        out[key] = value
    return out
