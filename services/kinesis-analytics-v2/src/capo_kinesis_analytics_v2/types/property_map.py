"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#PropertyMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.property_key
    import capo_kinesis_analytics_v2.types.property_value

PropertyMap: TypeAlias = dict[
    "capo_kinesis_analytics_v2.types.property_key.PropertyKey",
    "capo_kinesis_analytics_v2.types.property_value.PropertyValue",
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
