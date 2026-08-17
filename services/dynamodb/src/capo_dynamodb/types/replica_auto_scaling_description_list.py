"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaAutoScalingDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.replica_auto_scaling_description

ReplicaAutoScalingDescriptionList: TypeAlias = list[
    "capo_dynamodb.types.replica_auto_scaling_description.ReplicaAutoScalingDescription"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReplicaAutoScalingDescriptionList) -> list:
    import capo_dynamodb.types.replica_auto_scaling_description

    out: list = []
    for item in value:
        out.append(
            capo_dynamodb.types.replica_auto_scaling_description.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ReplicaAutoScalingDescriptionList:
    import capo_dynamodb.types.replica_auto_scaling_description

    out: ReplicaAutoScalingDescriptionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_dynamodb.types.replica_auto_scaling_description.deserialize_aws_json_1_0(
                item
            )
        )
    return out
