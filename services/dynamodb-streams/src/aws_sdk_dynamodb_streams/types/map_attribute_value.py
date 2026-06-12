"""Generated from Smithy shape ``com.amazonaws.dynamodbstreams#MapAttributeValue``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb_streams.types.attribute_name
    import aws_sdk_dynamodb_streams.types.attribute_value

MapAttributeValue: TypeAlias = dict[
    "aws_sdk_dynamodb_streams.types.attribute_name.AttributeName",
    "aws_sdk_dynamodb_streams.types.attribute_value.AttributeValue",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: MapAttributeValue) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_dynamodb_streams.types.attribute_value

        out[key] = (
            aws_sdk_dynamodb_streams.types.attribute_value.serialize_aws_json_1_0(value)
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> MapAttributeValue:
    out: MapAttributeValue = {}
    for key, value in data.items():
        import aws_sdk_dynamodb_streams.types.attribute_value

        out[key] = (
            aws_sdk_dynamodb_streams.types.attribute_value.deserialize_aws_json_1_0(
                value
            )
        )
    return out
