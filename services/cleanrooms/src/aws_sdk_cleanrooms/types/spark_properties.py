"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SparkProperties``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.spark_property_key
    import aws_sdk_cleanrooms.types.spark_property_value

SparkProperties: TypeAlias = dict[
    "aws_sdk_cleanrooms.types.spark_property_key.SparkPropertyKey",
    "aws_sdk_cleanrooms.types.spark_property_value.SparkPropertyValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: SparkProperties) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> SparkProperties:
    out: SparkProperties = {}
    for key, value in data.items():
        out[key] = value
    return out
