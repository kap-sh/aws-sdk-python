"""Generated from Smithy shape ``com.amazonaws.glue#ParametersMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.key_string
    import aws_sdk_glue.types.parameters_map_value

ParametersMap: TypeAlias = dict[
    "aws_sdk_glue.types.key_string.KeyString",
    "aws_sdk_glue.types.parameters_map_value.ParametersMapValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ParametersMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> ParametersMap:
    out: ParametersMap = {}
    for key, value in data.items():
        out[key] = value
    return out
