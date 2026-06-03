"""Generated from Smithy shape ``com.amazonaws.secretsmanager#AddReplicaRegionListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.replica_region_type

AddReplicaRegionListType: TypeAlias = list[
    "aws_sdk_secrets_manager.types.replica_region_type.ReplicaRegionType"
]
