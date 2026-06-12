"""Generated from Smithy shape ``com.amazonaws.wafv2#AttributeValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.attribute_value

AttributeValues: TypeAlias = list["aws_sdk_wafv2.types.attribute_value.AttributeValue"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttributeValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AttributeValues:
    return list(data)
