"""Generated from Smithy shape ``com.amazonaws.finspace#KxAttachedClusters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_finspace.types.kx_attached_cluster

KxAttachedClusters: TypeAlias = list[
    "aws_sdk_finspace.types.kx_attached_cluster.KxAttachedCluster"
]


# --- restJson1 ser/de ---
def serialize_json(value: KxAttachedClusters) -> list:
    import aws_sdk_finspace.types.kx_attached_cluster

    out: list = []
    for item in value:
        out.append(aws_sdk_finspace.types.kx_attached_cluster.serialize_json(item))
    return out


def deserialize_json(data: list) -> KxAttachedClusters:
    import aws_sdk_finspace.types.kx_attached_cluster

    out: KxAttachedClusters = []
    for item in data:
        out.append(aws_sdk_finspace.types.kx_attached_cluster.deserialize_json(item))
    return out
