"""Generated from Smithy shape ``com.amazonaws.pcs#GetComputeNodeGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_pcs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pcs.types.cluster_identifier
    import capo_pcs.types.compute_node_group_identifier


class GetComputeNodeGroupRequest(TypedDict, closed=True):
    cluster_identifier: "capo_pcs.types.cluster_identifier.ClusterIdentifier"
    """<p>The name or ID of the cluster.</p>"""
    compute_node_group_identifier: (
        "capo_pcs.types.compute_node_group_identifier.ComputeNodeGroupIdentifier"
    )
    """<p>The name or ID of the compute node group.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetComputeNodeGroupRequest) -> dict:
    out: dict = {}
    out["clusterIdentifier"] = value["cluster_identifier"]
    out["computeNodeGroupIdentifier"] = value["compute_node_group_identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetComputeNodeGroupRequest:
    out: GetComputeNodeGroupRequest = {}  # type: ignore[typeddict-item]
    if "clusterIdentifier" in data:
        out["cluster_identifier"] = data["clusterIdentifier"]
    else:
        raise DeserializationError(
            "GetComputeNodeGroupRequest.cluster_identifier required"
        )
    if "computeNodeGroupIdentifier" in data:
        out["compute_node_group_identifier"] = data["computeNodeGroupIdentifier"]
    else:
        raise DeserializationError(
            "GetComputeNodeGroupRequest.compute_node_group_identifier required"
        )
    return out
