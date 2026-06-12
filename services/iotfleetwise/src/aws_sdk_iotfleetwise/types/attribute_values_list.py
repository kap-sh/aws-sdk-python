"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#attributeValuesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.attribute_value

attributeValuesList: TypeAlias = list[
    "aws_sdk_iotfleetwise.types.attribute_value.attributeValue"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: attributeValuesList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> attributeValuesList:
    return list(data)
