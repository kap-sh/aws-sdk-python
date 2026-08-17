"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#Enumerations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.token_string
    import capo_cloudwatch_logs.types.token_value

Enumerations: TypeAlias = dict[
    "capo_cloudwatch_logs.types.token_string.TokenString",
    "capo_cloudwatch_logs.types.token_value.TokenValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: Enumerations) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> Enumerations:
    out: Enumerations = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
