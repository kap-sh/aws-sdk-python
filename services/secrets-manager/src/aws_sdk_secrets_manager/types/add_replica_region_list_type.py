"""Generated from Smithy shape ``com.amazonaws.secretsmanager#AddReplicaRegionListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.replica_region_type

AddReplicaRegionListType: TypeAlias = list[
    "aws_sdk_secrets_manager.types.replica_region_type.ReplicaRegionType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddReplicaRegionListType) -> list:
    import aws_sdk_secrets_manager.types.replica_region_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_secrets_manager.types.replica_region_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AddReplicaRegionListType:
    import aws_sdk_secrets_manager.types.replica_region_type

    out: AddReplicaRegionListType = []
    for item in data:
        out.append(
            aws_sdk_secrets_manager.types.replica_region_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
