"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#NatGatewayConfiguration``."""

from typing_extensions import NotRequired, TypedDict


class NatGatewayConfiguration(TypedDict, closed=True):
    active_connection_count: NotRequired["int"]
    """<p>The number of active connections through the NAT Gateway.</p>"""
    packets_in_from_source: NotRequired["int"]
    """<p>The number of packets received from the source through the NAT Gateway.</p>"""
    packets_in_from_destination: NotRequired["int"]
    """<p>The number of packets received from the destination through the NAT Gateway.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NatGatewayConfiguration) -> dict:
    out: dict = {}
    if "active_connection_count" in value:
        out["activeConnectionCount"] = value["active_connection_count"]
    if "packets_in_from_source" in value:
        out["packetsInFromSource"] = value["packets_in_from_source"]
    if "packets_in_from_destination" in value:
        out["packetsInFromDestination"] = value["packets_in_from_destination"]
    return out


def deserialize_aws_json_1_0(data: dict) -> NatGatewayConfiguration:
    out: NatGatewayConfiguration = {}  # type: ignore[typeddict-item]
    if "activeConnectionCount" in data:
        out["active_connection_count"] = data["activeConnectionCount"]
    if "packetsInFromSource" in data:
        out["packets_in_from_source"] = data["packetsInFromSource"]
    if "packetsInFromDestination" in data:
        out["packets_in_from_destination"] = data["packetsInFromDestination"]
    return out
