"""Generated from Smithy shape ``com.amazonaws.dynamodb#AttributeUpdates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.attribute_name
    import capo_dynamodb.types.attribute_value_update

AttributeUpdates: TypeAlias = dict[
    "capo_dynamodb.types.attribute_name.AttributeName",
    "capo_dynamodb.types.attribute_value_update.AttributeValueUpdate",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: AttributeUpdates) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_dynamodb.types.attribute_value_update

        out[key] = capo_dynamodb.types.attribute_value_update.serialize_aws_json_1_0(
            value
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AttributeUpdates:
    out: AttributeUpdates = {}
    for key, value in data.items():
        import capo_dynamodb.types.attribute_value_update

        out[key] = capo_dynamodb.types.attribute_value_update.deserialize_aws_json_1_0(
            value
        )
    return out
