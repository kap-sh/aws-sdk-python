"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ViewPropertiesMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.view_properties_key
    import aws_sdk_cloudtrail.types.view_properties_value

ViewPropertiesMap: TypeAlias = dict[
    "aws_sdk_cloudtrail.types.view_properties_key.ViewPropertiesKey",
    "aws_sdk_cloudtrail.types.view_properties_value.ViewPropertiesValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ViewPropertiesMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> ViewPropertiesMap:
    out: ViewPropertiesMap = {}
    for key, value in data.items():
        out[key] = value
    return out
