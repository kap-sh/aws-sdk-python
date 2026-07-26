"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaUpdateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.replica_update

ReplicaUpdateList: TypeAlias = list["capo_dynamodb.types.replica_update.ReplicaUpdate"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReplicaUpdateList) -> list:
    import capo_dynamodb.types.replica_update

    out: list = []
    for item in value:
        out.append(capo_dynamodb.types.replica_update.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ReplicaUpdateList:
    import capo_dynamodb.types.replica_update

    out: ReplicaUpdateList = []
    for item in data:
        out.append(capo_dynamodb.types.replica_update.deserialize_aws_json_1_0(item))
    return out
