"""Generated from Smithy shape ``com.amazonaws.dynamodb#AttributeNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.attribute_name

AttributeNameList: TypeAlias = list["capo_dynamodb.types.attribute_name.AttributeName"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AttributeNameList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> AttributeNameList:
    return [item for item in data if item is not None]
