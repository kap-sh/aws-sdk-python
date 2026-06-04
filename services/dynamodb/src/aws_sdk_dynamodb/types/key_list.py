"""Generated from Smithy shape ``com.amazonaws.dynamodb#KeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.key

KeyList: TypeAlias = list["aws_sdk_dynamodb.types.key.Key"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KeyList) -> list:
    import aws_sdk_dynamodb.types.key

    out: list = []
    for item in value:
        out.append(aws_sdk_dynamodb.types.key.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> KeyList:
    import aws_sdk_dynamodb.types.key

    out: KeyList = []
    for item in data:
        out.append(aws_sdk_dynamodb.types.key.deserialize_aws_json_1_0(item))
    return out
