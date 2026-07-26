"""Generated from Smithy shape ``com.amazonaws.emrcontainers#VirtualClusterStates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr_containers.types.virtual_cluster_state

VirtualClusterStates: TypeAlias = list[
    "capo_emr_containers.types.virtual_cluster_state.VirtualClusterState"
]


# --- restJson1 ser/de ---
def serialize_json(value: VirtualClusterStates) -> list:
    import capo_emr_containers.types.virtual_cluster_state

    out: list = []
    for item in value:
        out.append(capo_emr_containers.types.virtual_cluster_state.serialize_json(item))
    return out


def deserialize_json(data: list) -> VirtualClusterStates:
    import capo_emr_containers.types.virtual_cluster_state

    out: VirtualClusterStates = []
    for item in data:
        out.append(
            capo_emr_containers.types.virtual_cluster_state.deserialize_json(item)
        )
    return out
