"""Generated from Smithy shape ``com.amazonaws.dynamodb#LocalSecondaryIndexes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.local_secondary_index_info

LocalSecondaryIndexes: TypeAlias = list[
    "aws_sdk_dynamodb.types.local_secondary_index_info.LocalSecondaryIndexInfo"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LocalSecondaryIndexes) -> list:
    import aws_sdk_dynamodb.types.local_secondary_index_info

    out: list = []
    for item in value:
        out.append(
            aws_sdk_dynamodb.types.local_secondary_index_info.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> LocalSecondaryIndexes:
    import aws_sdk_dynamodb.types.local_secondary_index_info

    out: LocalSecondaryIndexes = []
    for item in data:
        out.append(
            aws_sdk_dynamodb.types.local_secondary_index_info.deserialize_aws_json_1_0(
                item
            )
        )
    return out
