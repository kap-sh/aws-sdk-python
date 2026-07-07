"""Generated from Smithy shape ``com.amazonaws.mediaconnect#GatewayNetwork``."""

from typing_extensions import NotRequired, TypedDict


class GatewayNetwork(TypedDict, closed=True):
    cidr_block: NotRequired["str"]
    """<p>A unique IP address range to use for this network. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16. </p>"""
    name: NotRequired["str"]
    """<p>The name of the network. This name is used to reference the network and must be unique among networks in this gateway. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GatewayNetwork) -> dict:
    out: dict = {}
    if "cidr_block" in value:
        out["cidrBlock"] = value["cidr_block"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> GatewayNetwork:
    out: GatewayNetwork = {}  # type: ignore[typeddict-item]
    if "cidrBlock" in data:
        out["cidr_block"] = data["cidrBlock"]
    if "name" in data:
        out["name"] = data["name"]
    return out
