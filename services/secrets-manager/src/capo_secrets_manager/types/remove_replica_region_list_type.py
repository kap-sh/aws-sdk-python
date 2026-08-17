"""Generated from Smithy shape ``com.amazonaws.secretsmanager#RemoveReplicaRegionListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_secrets_manager.types.region_type

RemoveReplicaRegionListType: TypeAlias = list[
    "capo_secrets_manager.types.region_type.RegionType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveReplicaRegionListType) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> RemoveReplicaRegionListType:
    return [item for item in data if item is not None]
