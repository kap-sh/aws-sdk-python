"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#EntityAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.entity_attributes_key
    import aws_sdk_cloudwatch_logs.types.entity_attributes_value

EntityAttributes: TypeAlias = dict[
    "aws_sdk_cloudwatch_logs.types.entity_attributes_key.EntityAttributesKey",
    "aws_sdk_cloudwatch_logs.types.entity_attributes_value.EntityAttributesValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: EntityAttributes) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> EntityAttributes:
    out: EntityAttributes = {}
    for key, value in data.items():
        out[key] = value
    return out
