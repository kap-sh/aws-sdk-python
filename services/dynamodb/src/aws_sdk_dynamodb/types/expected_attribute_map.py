"""Generated from Smithy shape ``com.amazonaws.dynamodb#ExpectedAttributeMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.attribute_name
    import aws_sdk_dynamodb.types.expected_attribute_value

ExpectedAttributeMap: TypeAlias = dict[
    "aws_sdk_dynamodb.types.attribute_name.AttributeName",
    "aws_sdk_dynamodb.types.expected_attribute_value.ExpectedAttributeValue",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: ExpectedAttributeMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_dynamodb.types.expected_attribute_value

        out[key] = (
            aws_sdk_dynamodb.types.expected_attribute_value.serialize_aws_json_1_0(
                value
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ExpectedAttributeMap:
    out: ExpectedAttributeMap = {}
    for key, value in data.items():
        import aws_sdk_dynamodb.types.expected_attribute_value

        out[key] = (
            aws_sdk_dynamodb.types.expected_attribute_value.deserialize_aws_json_1_0(
                value
            )
        )
    return out
