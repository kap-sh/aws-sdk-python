"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaGlobalSecondaryIndexAutoScalingDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.replica_global_secondary_index_auto_scaling_description

ReplicaGlobalSecondaryIndexAutoScalingDescriptionList: TypeAlias = list[
    "aws_sdk_dynamodb.types.replica_global_secondary_index_auto_scaling_description.ReplicaGlobalSecondaryIndexAutoScalingDescription"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: ReplicaGlobalSecondaryIndexAutoScalingDescriptionList,
) -> list:
    import aws_sdk_dynamodb.types.replica_global_secondary_index_auto_scaling_description

    out: list = []
    for item in value:
        out.append(
            aws_sdk_dynamodb.types.replica_global_secondary_index_auto_scaling_description.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: list,
) -> ReplicaGlobalSecondaryIndexAutoScalingDescriptionList:
    import aws_sdk_dynamodb.types.replica_global_secondary_index_auto_scaling_description

    out: ReplicaGlobalSecondaryIndexAutoScalingDescriptionList = []
    for item in data:
        out.append(
            aws_sdk_dynamodb.types.replica_global_secondary_index_auto_scaling_description.deserialize_aws_json_1_0(
                item
            )
        )
    return out
