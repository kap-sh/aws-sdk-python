"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaUpdateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.replica_update

ReplicaUpdateList: TypeAlias = list[
    "aws_sdk_dynamodb.types.replica_update.ReplicaUpdate"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReplicaUpdateList) -> list:
    import aws_sdk_dynamodb.types.replica_update

    out: list = []
    for item in value:
        out.append(aws_sdk_dynamodb.types.replica_update.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ReplicaUpdateList:
    import aws_sdk_dynamodb.types.replica_update

    out: ReplicaUpdateList = []
    for item in data:
        out.append(aws_sdk_dynamodb.types.replica_update.deserialize_aws_json_1_0(item))
    return out
