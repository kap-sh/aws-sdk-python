"""Generated from Smithy shape ``com.amazonaws.dynamodb#MapAttributeValue``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.attribute_name
    import capo_dynamodb.types.attribute_value

MapAttributeValue: TypeAlias = dict[
    "capo_dynamodb.types.attribute_name.AttributeName",
    "capo_dynamodb.types.attribute_value.AttributeValue",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: MapAttributeValue) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_dynamodb.types.attribute_value

        out[key] = capo_dynamodb.types.attribute_value.serialize_aws_json_1_0(value)
    return out


def deserialize_aws_json_1_0(data: dict) -> MapAttributeValue:
    out: MapAttributeValue = {}
    for key, value in data.items():
        import capo_dynamodb.types.attribute_value

        out[key] = capo_dynamodb.types.attribute_value.deserialize_aws_json_1_0(value)
    return out
