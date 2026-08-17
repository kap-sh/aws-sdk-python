"""Generated from Smithy shape ``com.amazonaws.dynamodb#BinarySetAttributeValue``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.binary_attribute_value

BinarySetAttributeValue: TypeAlias = list[
    "capo_dynamodb.types.binary_attribute_value.BinaryAttributeValue"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BinarySetAttributeValue) -> list:
    import capo_dynamodb.types.binary_attribute_value

    out: list = []
    for item in value:
        out.append(
            capo_dynamodb.types.binary_attribute_value.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BinarySetAttributeValue:
    import capo_dynamodb.types.binary_attribute_value

    out: BinarySetAttributeValue = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_dynamodb.types.binary_attribute_value.deserialize_aws_json_1_0(item)
        )
    return out
