"""Generated from Smithy shape ``com.amazonaws.dynamodbstreams#KeySchema``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb_streams.types.key_schema_element

KeySchema: TypeAlias = list[
    "aws_sdk_dynamodb_streams.types.key_schema_element.KeySchemaElement"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KeySchema) -> list:
    import aws_sdk_dynamodb_streams.types.key_schema_element

    out: list = []
    for item in value:
        out.append(
            aws_sdk_dynamodb_streams.types.key_schema_element.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> KeySchema:
    import aws_sdk_dynamodb_streams.types.key_schema_element

    out: KeySchema = []
    for item in data:
        out.append(
            aws_sdk_dynamodb_streams.types.key_schema_element.deserialize_aws_json_1_0(
                item
            )
        )
    return out
