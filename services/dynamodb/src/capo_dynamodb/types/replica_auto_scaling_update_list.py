"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaAutoScalingUpdateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.replica_auto_scaling_update

ReplicaAutoScalingUpdateList: TypeAlias = list[
    "capo_dynamodb.types.replica_auto_scaling_update.ReplicaAutoScalingUpdate"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReplicaAutoScalingUpdateList) -> list:
    import capo_dynamodb.types.replica_auto_scaling_update

    out: list = []
    for item in value:
        out.append(
            capo_dynamodb.types.replica_auto_scaling_update.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ReplicaAutoScalingUpdateList:
    import capo_dynamodb.types.replica_auto_scaling_update

    out: ReplicaAutoScalingUpdateList = []
    for item in data:
        out.append(
            capo_dynamodb.types.replica_auto_scaling_update.deserialize_aws_json_1_0(
                item
            )
        )
    return out
