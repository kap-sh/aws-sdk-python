"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#EntityKeyAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.entity_key_attributes_key
    import capo_cloudwatch_logs.types.entity_key_attributes_value

EntityKeyAttributes: TypeAlias = dict[
    "capo_cloudwatch_logs.types.entity_key_attributes_key.EntityKeyAttributesKey",
    "capo_cloudwatch_logs.types.entity_key_attributes_value.EntityKeyAttributesValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: EntityKeyAttributes) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> EntityKeyAttributes:
    out: EntityKeyAttributes = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
