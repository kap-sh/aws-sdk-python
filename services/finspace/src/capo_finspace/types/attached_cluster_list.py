"""Generated from Smithy shape ``com.amazonaws.finspace#AttachedClusterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_finspace.types.kx_cluster_name

AttachedClusterList: TypeAlias = list[
    "capo_finspace.types.kx_cluster_name.KxClusterName"
]


# --- restJson1 ser/de ---
def serialize_json(value: AttachedClusterList) -> list:
    return list(value)


def deserialize_json(data: list) -> AttachedClusterList:
    return list(data)
