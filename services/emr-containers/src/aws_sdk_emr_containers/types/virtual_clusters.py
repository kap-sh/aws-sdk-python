"""Generated from Smithy shape ``com.amazonaws.emrcontainers#VirtualClusters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.virtual_cluster

VirtualClusters: TypeAlias = list[
    "aws_sdk_emr_containers.types.virtual_cluster.VirtualCluster"
]


# --- restJson1 ser/de ---
def serialize_json(value: VirtualClusters) -> list:
    import aws_sdk_emr_containers.types.virtual_cluster

    out: list = []
    for item in value:
        out.append(aws_sdk_emr_containers.types.virtual_cluster.serialize_json(item))
    return out


def deserialize_json(data: list) -> VirtualClusters:
    import aws_sdk_emr_containers.types.virtual_cluster

    out: VirtualClusters = []
    for item in data:
        out.append(aws_sdk_emr_containers.types.virtual_cluster.deserialize_json(item))
    return out
