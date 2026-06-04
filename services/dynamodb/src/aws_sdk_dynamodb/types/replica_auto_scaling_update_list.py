"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaAutoScalingUpdateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.replica_auto_scaling_update

ReplicaAutoScalingUpdateList: TypeAlias = list[
    "aws_sdk_dynamodb.types.replica_auto_scaling_update.ReplicaAutoScalingUpdate"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReplicaAutoScalingUpdateList) -> list:
    import aws_sdk_dynamodb.types.replica_auto_scaling_update

    out: list = []
    for item in value:
        out.append(
            aws_sdk_dynamodb.types.replica_auto_scaling_update.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ReplicaAutoScalingUpdateList:
    import aws_sdk_dynamodb.types.replica_auto_scaling_update

    out: ReplicaAutoScalingUpdateList = []
    for item in data:
        out.append(
            aws_sdk_dynamodb.types.replica_auto_scaling_update.deserialize_aws_json_1_0(
                item
            )
        )
    return out
