"""Generated from Smithy shape ``com.amazonaws.dynamodb#AttributeDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.attribute_definition

AttributeDefinitions: TypeAlias = list[
    "capo_dynamodb.types.attribute_definition.AttributeDefinition"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AttributeDefinitions) -> list:
    import capo_dynamodb.types.attribute_definition

    out: list = []
    for item in value:
        out.append(
            capo_dynamodb.types.attribute_definition.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AttributeDefinitions:
    import capo_dynamodb.types.attribute_definition

    out: AttributeDefinitions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_dynamodb.types.attribute_definition.deserialize_aws_json_1_0(item)
        )
    return out
