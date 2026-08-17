"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaGlobalSecondaryIndexAutoScalingUpdateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.replica_global_secondary_index_auto_scaling_update

ReplicaGlobalSecondaryIndexAutoScalingUpdateList: TypeAlias = list[
    "capo_dynamodb.types.replica_global_secondary_index_auto_scaling_update.ReplicaGlobalSecondaryIndexAutoScalingUpdate"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: ReplicaGlobalSecondaryIndexAutoScalingUpdateList,
) -> list:
    import capo_dynamodb.types.replica_global_secondary_index_auto_scaling_update

    out: list = []
    for item in value:
        out.append(
            capo_dynamodb.types.replica_global_secondary_index_auto_scaling_update.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: list,
) -> ReplicaGlobalSecondaryIndexAutoScalingUpdateList:
    import capo_dynamodb.types.replica_global_secondary_index_auto_scaling_update

    out: ReplicaGlobalSecondaryIndexAutoScalingUpdateList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_dynamodb.types.replica_global_secondary_index_auto_scaling_update.deserialize_aws_json_1_0(
                item
            )
        )
    return out
