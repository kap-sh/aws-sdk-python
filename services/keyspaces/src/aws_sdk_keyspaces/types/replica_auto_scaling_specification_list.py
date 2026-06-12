"""Generated from Smithy shape ``com.amazonaws.keyspaces#ReplicaAutoScalingSpecificationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_keyspaces.types.replica_auto_scaling_specification

ReplicaAutoScalingSpecificationList: TypeAlias = list[
    "aws_sdk_keyspaces.types.replica_auto_scaling_specification.ReplicaAutoScalingSpecification"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReplicaAutoScalingSpecificationList) -> list:
    import aws_sdk_keyspaces.types.replica_auto_scaling_specification

    out: list = []
    for item in value:
        out.append(
            aws_sdk_keyspaces.types.replica_auto_scaling_specification.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ReplicaAutoScalingSpecificationList:
    import aws_sdk_keyspaces.types.replica_auto_scaling_specification

    out: ReplicaAutoScalingSpecificationList = []
    for item in data:
        out.append(
            aws_sdk_keyspaces.types.replica_auto_scaling_specification.deserialize_aws_json_1_0(
                item
            )
        )
    return out
