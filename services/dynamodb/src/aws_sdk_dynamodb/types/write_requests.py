"""Generated from Smithy shape ``com.amazonaws.dynamodb#WriteRequests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.write_request

WriteRequests: TypeAlias = list["aws_sdk_dynamodb.types.write_request.WriteRequest"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WriteRequests) -> list:
    import aws_sdk_dynamodb.types.write_request

    out: list = []
    for item in value:
        out.append(aws_sdk_dynamodb.types.write_request.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> WriteRequests:
    import aws_sdk_dynamodb.types.write_request

    out: WriteRequests = []
    for item in data:
        out.append(aws_sdk_dynamodb.types.write_request.deserialize_aws_json_1_0(item))
    return out
