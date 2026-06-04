"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaGlobalSecondaryIndexList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.replica_global_secondary_index

ReplicaGlobalSecondaryIndexList: TypeAlias = list[
    "aws_sdk_dynamodb.types.replica_global_secondary_index.ReplicaGlobalSecondaryIndex"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReplicaGlobalSecondaryIndexList) -> list:
    import aws_sdk_dynamodb.types.replica_global_secondary_index

    out: list = []
    for item in value:
        out.append(
            aws_sdk_dynamodb.types.replica_global_secondary_index.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ReplicaGlobalSecondaryIndexList:
    import aws_sdk_dynamodb.types.replica_global_secondary_index

    out: ReplicaGlobalSecondaryIndexList = []
    for item in data:
        out.append(
            aws_sdk_dynamodb.types.replica_global_secondary_index.deserialize_aws_json_1_0(
                item
            )
        )
    return out
