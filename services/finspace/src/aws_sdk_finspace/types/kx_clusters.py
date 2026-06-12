"""Generated from Smithy shape ``com.amazonaws.finspace#KxClusters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_finspace.types.kx_cluster

KxClusters: TypeAlias = list["aws_sdk_finspace.types.kx_cluster.KxCluster"]


# --- restJson1 ser/de ---
def serialize_json(value: KxClusters) -> list:
    import aws_sdk_finspace.types.kx_cluster

    out: list = []
    for item in value:
        out.append(aws_sdk_finspace.types.kx_cluster.serialize_json(item))
    return out


def deserialize_json(data: list) -> KxClusters:
    import aws_sdk_finspace.types.kx_cluster

    out: KxClusters = []
    for item in data:
        out.append(aws_sdk_finspace.types.kx_cluster.deserialize_json(item))
    return out
