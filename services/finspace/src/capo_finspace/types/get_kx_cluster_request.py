"""Generated from Smithy shape ``com.amazonaws.finspace#GetKxClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.kx_cluster_name
    import capo_finspace.types.kx_environment_id


class GetKxClusterRequest(TypedDict, closed=True):
    environment_id: "capo_finspace.types.kx_environment_id.KxEnvironmentId"
    """<p>A unique identifier for the kdb environment.</p>"""
    cluster_name: "capo_finspace.types.kx_cluster_name.KxClusterName"
    """<p>The name of the cluster that you want to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetKxClusterRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetKxClusterRequest:
    out: GetKxClusterRequest = {}  # type: ignore[typeddict-item]
    return out
