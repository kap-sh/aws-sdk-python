"""Generated from Smithy shape ``com.amazonaws.dynamodb#StringSetAttributeValue``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.string_attribute_value

StringSetAttributeValue: TypeAlias = list[
    "capo_dynamodb.types.string_attribute_value.StringAttributeValue"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StringSetAttributeValue) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> StringSetAttributeValue:
    return list(data)
