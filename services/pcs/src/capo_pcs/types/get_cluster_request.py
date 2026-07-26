"""Generated from Smithy shape ``com.amazonaws.pcs#GetClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_pcs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pcs.types.cluster_identifier


class GetClusterRequest(TypedDict, closed=True):
    cluster_identifier: "capo_pcs.types.cluster_identifier.ClusterIdentifier"
    """<p>The name or ID of the cluster.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetClusterRequest) -> dict:
    out: dict = {}
    out["clusterIdentifier"] = value["cluster_identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetClusterRequest:
    out: GetClusterRequest = {}  # type: ignore[typeddict-item]
    if "clusterIdentifier" in data:
        out["cluster_identifier"] = data["clusterIdentifier"]
    else:
        raise DeserializationError("GetClusterRequest.cluster_identifier required")
    return out
