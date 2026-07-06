"""Generated from Smithy shape ``com.amazonaws.mediaconnect#EgressGatewayBridge``."""

from typing_extensions import NotRequired, TypedDict


class EgressGatewayBridge(TypedDict, closed=True):
    instance_id: NotRequired["str"]
    """<p> The ID of the instance running this bridge.</p>"""
    max_bitrate: NotRequired["int"]
    """<p> The maximum expected bitrate (in bps) of the egress bridge.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EgressGatewayBridge) -> dict:
    out: dict = {}
    if "instance_id" in value:
        out["instanceId"] = value["instance_id"]
    if "max_bitrate" in value:
        out["maxBitrate"] = value["max_bitrate"]
    return out


def deserialize_json(data: dict) -> EgressGatewayBridge:
    out: EgressGatewayBridge = {}  # type: ignore[typeddict-item]
    if "instanceId" in data:
        out["instance_id"] = data["instanceId"]
    if "maxBitrate" in data:
        out["max_bitrate"] = data["maxBitrate"]
    return out
