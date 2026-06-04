"""Generated from Smithy shape ``com.amazonaws.dynamodb#AttributeValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.attribute_value

AttributeValueList: TypeAlias = list[
    "aws_sdk_dynamodb.types.attribute_value.AttributeValue"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AttributeValueList) -> list:
    import aws_sdk_dynamodb.types.attribute_value

    out: list = []
    for item in value:
        out.append(aws_sdk_dynamodb.types.attribute_value.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> AttributeValueList:
    import aws_sdk_dynamodb.types.attribute_value

    out: AttributeValueList = []
    for item in data:
        out.append(
            aws_sdk_dynamodb.types.attribute_value.deserialize_aws_json_1_0(item)
        )
    return out
