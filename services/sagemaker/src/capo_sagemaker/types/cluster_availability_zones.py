"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterAvailabilityZones``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_availability_zone

ClusterAvailabilityZones: TypeAlias = list[
    "capo_sagemaker.types.cluster_availability_zone.ClusterAvailabilityZone"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterAvailabilityZones) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ClusterAvailabilityZones:
    return list(data)
