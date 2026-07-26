"""Generated from Smithy shape ``com.amazonaws.emrcontainers#VirtualClusters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr_containers.types.virtual_cluster

VirtualClusters: TypeAlias = list[
    "capo_emr_containers.types.virtual_cluster.VirtualCluster"
]


# --- restJson1 ser/de ---
def serialize_json(value: VirtualClusters) -> list:
    import capo_emr_containers.types.virtual_cluster

    out: list = []
    for item in value:
        out.append(capo_emr_containers.types.virtual_cluster.serialize_json(item))
    return out


def deserialize_json(data: list) -> VirtualClusters:
    import capo_emr_containers.types.virtual_cluster

    out: VirtualClusters = []
    for item in data:
        out.append(capo_emr_containers.types.virtual_cluster.deserialize_json(item))
    return out
