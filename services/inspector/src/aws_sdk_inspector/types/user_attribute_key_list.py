"""Generated from Smithy shape ``com.amazonaws.inspector#UserAttributeKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector.types.attribute_key

UserAttributeKeyList: TypeAlias = list[
    "aws_sdk_inspector.types.attribute_key.AttributeKey"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserAttributeKeyList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> UserAttributeKeyList:
    return list(data)
