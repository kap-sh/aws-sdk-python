"""Generated from Smithy shape ``com.amazonaws.mgn#TargetNetwork``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mgn.types.cidr
    import capo_mgn.types.target_network_topology


class TargetNetwork(TypedDict, closed=True):
    topology: "capo_mgn.types.target_network_topology.TargetNetworkTopology"
    """<p>The network topology type for the target environment.</p>"""
    inbound_cidr: NotRequired["capo_mgn.types.cidr.Cidr"]
    """<p>The CIDR block for inbound traffic in the target network.</p>"""
    outbound_cidr: NotRequired["capo_mgn.types.cidr.Cidr"]
    """<p>The CIDR block for outbound traffic in the target network.</p>"""
    inspection_cidr: NotRequired["capo_mgn.types.cidr.Cidr"]
    """<p>The CIDR block for inspection traffic in the target network.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TargetNetwork) -> dict:
    out: dict = {}
    out["topology"] = value["topology"]
    if "inbound_cidr" in value:
        out["inboundCidr"] = value["inbound_cidr"]
    if "outbound_cidr" in value:
        out["outboundCidr"] = value["outbound_cidr"]
    if "inspection_cidr" in value:
        out["inspectionCidr"] = value["inspection_cidr"]
    return out


def deserialize_json(data: dict) -> TargetNetwork:
    out: TargetNetwork = {}  # type: ignore[typeddict-item]
    if "topology" in data:
        out["topology"] = data["topology"]
    else:
        raise DeserializationError("TargetNetwork.topology required")
    if "inboundCidr" in data:
        out["inbound_cidr"] = data["inboundCidr"]
    if "outboundCidr" in data:
        out["outbound_cidr"] = data["outboundCidr"]
    if "inspectionCidr" in data:
        out["inspection_cidr"] = data["inspectionCidr"]
    return out
