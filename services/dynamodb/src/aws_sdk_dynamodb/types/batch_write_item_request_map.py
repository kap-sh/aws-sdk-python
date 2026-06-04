"""Generated from Smithy shape ``com.amazonaws.dynamodb#BatchWriteItemRequestMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.table_arn
    import aws_sdk_dynamodb.types.write_requests

BatchWriteItemRequestMap: TypeAlias = dict[
    "aws_sdk_dynamodb.types.table_arn.TableArn",
    "aws_sdk_dynamodb.types.write_requests.WriteRequests",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: BatchWriteItemRequestMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_dynamodb.types.write_requests

        out[key] = aws_sdk_dynamodb.types.write_requests.serialize_aws_json_1_0(value)
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchWriteItemRequestMap:
    out: BatchWriteItemRequestMap = {}
    for key, value in data.items():
        import aws_sdk_dynamodb.types.write_requests

        out[key] = aws_sdk_dynamodb.types.write_requests.deserialize_aws_json_1_0(value)
    return out
