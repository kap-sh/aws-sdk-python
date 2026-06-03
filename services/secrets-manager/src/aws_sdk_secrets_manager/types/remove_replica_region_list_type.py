"""Generated from Smithy shape ``com.amazonaws.secretsmanager#RemoveReplicaRegionListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.region_type

RemoveReplicaRegionListType: TypeAlias = list[
    "aws_sdk_secrets_manager.types.region_type.RegionType"
]
