"""Generated from Smithy shape ``com.amazonaws.finspace#KxClusterNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_finspace.types.kx_cluster_name

KxClusterNameList: TypeAlias = list["capo_finspace.types.kx_cluster_name.KxClusterName"]


# --- restJson1 ser/de ---
def serialize_json(value: KxClusterNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> KxClusterNameList:
    return list(data)
