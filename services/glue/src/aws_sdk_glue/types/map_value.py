"""Generated from Smithy shape ``com.amazonaws.glue#MapValue``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.generic_string

MapValue: TypeAlias = dict[
    "aws_sdk_glue.types.generic_string.GenericString",
    "aws_sdk_glue.types.generic_string.GenericString",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: MapValue) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> MapValue:
    out: MapValue = {}
    for key, value in data.items():
        out[key] = value
    return out
