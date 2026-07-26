"""Generated from Smithy shape ``com.amazonaws.dynamodb#NonKeyAttributeNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.non_key_attribute_name

NonKeyAttributeNameList: TypeAlias = list[
    "capo_dynamodb.types.non_key_attribute_name.NonKeyAttributeName"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NonKeyAttributeNameList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> NonKeyAttributeNameList:
    return list(data)
