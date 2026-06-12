"""Generated from Smithy shape ``com.amazonaws.finspace#DeleteKxClusterNodeRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace.types.kx_cluster_name
    import aws_sdk_finspace.types.kx_cluster_node_id_string
    import aws_sdk_finspace.types.kx_environment_id


class DeleteKxClusterNodeRequest(TypedDict):
    environment_id: "aws_sdk_finspace.types.kx_environment_id.KxEnvironmentId"
    """<p>A unique identifier for the kdb environment.</p>"""
    cluster_name: "aws_sdk_finspace.types.kx_cluster_name.KxClusterName"
    """<p>The name of the cluster, for which you want to delete the nodes.</p>"""
    node_id: "aws_sdk_finspace.types.kx_cluster_node_id_string.KxClusterNodeIdString"
    """<p>A unique identifier for the node that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteKxClusterNodeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteKxClusterNodeRequest:
    out: DeleteKxClusterNodeRequest = {}  # type: ignore[typeddict-item]
    return out
