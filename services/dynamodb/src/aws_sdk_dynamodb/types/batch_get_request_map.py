"""Generated from Smithy shape ``com.amazonaws.dynamodb#BatchGetRequestMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.keys_and_attributes
    import aws_sdk_dynamodb.types.table_arn

BatchGetRequestMap: TypeAlias = dict[
    "aws_sdk_dynamodb.types.table_arn.TableArn",
    "aws_sdk_dynamodb.types.keys_and_attributes.KeysAndAttributes",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: BatchGetRequestMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_dynamodb.types.keys_and_attributes

        out[key] = aws_sdk_dynamodb.types.keys_and_attributes.serialize_aws_json_1_0(
            value
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchGetRequestMap:
    out: BatchGetRequestMap = {}
    for key, value in data.items():
        import aws_sdk_dynamodb.types.keys_and_attributes

        out[key] = aws_sdk_dynamodb.types.keys_and_attributes.deserialize_aws_json_1_0(
            value
        )
    return out
