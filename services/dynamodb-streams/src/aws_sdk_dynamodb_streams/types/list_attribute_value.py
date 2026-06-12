"""Generated from Smithy shape ``com.amazonaws.dynamodbstreams#ListAttributeValue``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb_streams.types.attribute_value

ListAttributeValue: TypeAlias = list[
    "aws_sdk_dynamodb_streams.types.attribute_value.AttributeValue"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAttributeValue) -> list:
    import aws_sdk_dynamodb_streams.types.attribute_value

    out: list = []
    for item in value:
        out.append(
            aws_sdk_dynamodb_streams.types.attribute_value.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ListAttributeValue:
    import aws_sdk_dynamodb_streams.types.attribute_value

    out: ListAttributeValue = []
    for item in data:
        out.append(
            aws_sdk_dynamodb_streams.types.attribute_value.deserialize_aws_json_1_0(
                item
            )
        )
    return out
