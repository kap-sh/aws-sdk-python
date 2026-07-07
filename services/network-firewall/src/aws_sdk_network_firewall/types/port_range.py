"""Generated from Smithy shape ``com.amazonaws.networkfirewall#PortRange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.port_range_bound


class PortRange(TypedDict, closed=True):
    from_port: "aws_sdk_network_firewall.types.port_range_bound.PortRangeBound"
    """<p>The lower limit of the port range. This must be less than or equal to the <code>ToPort</code> specification. </p>"""
    to_port: "aws_sdk_network_firewall.types.port_range_bound.PortRangeBound"
    """<p>The upper limit of the port range. This must be greater than or equal to the <code>FromPort</code> specification. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PortRange) -> dict:
    out: dict = {}
    out["FromPort"] = value.get("from_port", 0)
    out["ToPort"] = value.get("to_port", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> PortRange:
    out: PortRange = {}  # type: ignore[typeddict-item]
    if "FromPort" in data:
        out["from_port"] = data["FromPort"]
    else:
        out["from_port"] = 0
    if "ToPort" in data:
        out["to_port"] = data["ToPort"]
    else:
        out["to_port"] = 0
    return out
