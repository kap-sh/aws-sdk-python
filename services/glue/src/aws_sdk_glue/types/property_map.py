"""Generated from Smithy shape ``com.amazonaws.glue#PropertyMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.property_key
    import aws_sdk_glue.types.property_value

PropertyMap: TypeAlias = dict[
    "aws_sdk_glue.types.property_key.PropertyKey",
    "aws_sdk_glue.types.property_value.PropertyValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: PropertyMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> PropertyMap:
    out: PropertyMap = {}
    for key, value in data.items():
        out[key] = value
    return out
