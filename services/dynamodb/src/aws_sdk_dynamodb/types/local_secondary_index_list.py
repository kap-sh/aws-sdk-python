"""Generated from Smithy shape ``com.amazonaws.dynamodb#LocalSecondaryIndexList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.local_secondary_index

LocalSecondaryIndexList: TypeAlias = list[
    "aws_sdk_dynamodb.types.local_secondary_index.LocalSecondaryIndex"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LocalSecondaryIndexList) -> list:
    import aws_sdk_dynamodb.types.local_secondary_index

    out: list = []
    for item in value:
        out.append(
            aws_sdk_dynamodb.types.local_secondary_index.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> LocalSecondaryIndexList:
    import aws_sdk_dynamodb.types.local_secondary_index

    out: LocalSecondaryIndexList = []
    for item in data:
        out.append(
            aws_sdk_dynamodb.types.local_secondary_index.deserialize_aws_json_1_0(item)
        )
    return out
