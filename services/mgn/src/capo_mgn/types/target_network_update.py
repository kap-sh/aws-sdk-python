"""Generated from Smithy shape ``com.amazonaws.mgn#TargetNetworkUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.cidr
    import capo_mgn.types.target_network_topology


class TargetNetworkUpdate(TypedDict, closed=True):
    topology: NotRequired[
        "capo_mgn.types.target_network_topology.TargetNetworkTopology"
    ]
    """<p>The updated network topology type.</p>"""
    inbound_cidr: NotRequired["capo_mgn.types.cidr.Cidr"]
    """<p>The updated CIDR block for inbound traffic.</p>"""
    outbound_cidr: NotRequired["capo_mgn.types.cidr.Cidr"]
    """<p>The updated CIDR block for outbound traffic.</p>"""
    inspection_cidr: NotRequired["capo_mgn.types.cidr.Cidr"]
    """<p>The updated CIDR block for inspection traffic.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TargetNetworkUpdate) -> dict:
    out: dict = {}
    if "topology" in value:
        out["topology"] = value["topology"]
    if "inbound_cidr" in value:
        out["inboundCidr"] = value["inbound_cidr"]
    if "outbound_cidr" in value:
        out["outboundCidr"] = value["outbound_cidr"]
    if "inspection_cidr" in value:
        out["inspectionCidr"] = value["inspection_cidr"]
    return out


def deserialize_json(data: dict) -> TargetNetworkUpdate:
    out: TargetNetworkUpdate = {}  # type: ignore[typeddict-item]
    if "topology" in data:
        out["topology"] = data["topology"]
    if "inboundCidr" in data:
        out["inbound_cidr"] = data["inboundCidr"]
    if "outboundCidr" in data:
        out["outbound_cidr"] = data["outboundCidr"]
    if "inspectionCidr" in data:
        out["inspection_cidr"] = data["inspectionCidr"]
    return out
