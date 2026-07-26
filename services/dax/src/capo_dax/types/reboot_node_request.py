"""Generated from Smithy shape ``com.amazonaws.dax#RebootNodeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_dax.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dax.types.string


class RebootNodeRequest(TypedDict, closed=True):
    cluster_name: "capo_dax.types.string.String"
    """<p>The name of the DAX cluster containing the node to be rebooted.</p>"""
    node_id: "capo_dax.types.string.String"
    """<p>The system-assigned ID of the node to be rebooted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RebootNodeRequest) -> dict:
    out: dict = {}
    out["ClusterName"] = value["cluster_name"]
    out["NodeId"] = value["node_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RebootNodeRequest:
    out: RebootNodeRequest = {}  # type: ignore[typeddict-item]
    if "ClusterName" in data:
        out["cluster_name"] = data["ClusterName"]
    else:
        raise DeserializationError("RebootNodeRequest.cluster_name required")
    if "NodeId" in data:
        out["node_id"] = data["NodeId"]
    else:
        raise DeserializationError("RebootNodeRequest.node_id required")
    return out
