"""Generated from Smithy shape ``com.amazonaws.pricing#AttributeValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pricing.types.attribute_value

AttributeValueList: TypeAlias = list[
    "aws_sdk_pricing.types.attribute_value.AttributeValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttributeValueList) -> list:
    import aws_sdk_pricing.types.attribute_value

    out: list = []
    for item in value:
        out.append(aws_sdk_pricing.types.attribute_value.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AttributeValueList:
    import aws_sdk_pricing.types.attribute_value

    out: AttributeValueList = []
    for item in data:
        out.append(aws_sdk_pricing.types.attribute_value.deserialize_aws_json_1_1(item))
    return out
