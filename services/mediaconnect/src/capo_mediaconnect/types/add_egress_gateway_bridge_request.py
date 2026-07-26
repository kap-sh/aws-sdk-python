"""Generated from Smithy shape ``com.amazonaws.mediaconnect#AddEgressGatewayBridgeRequest``."""

from typing_extensions import NotRequired, TypedDict


class AddEgressGatewayBridgeRequest(TypedDict, closed=True):
    max_bitrate: NotRequired["int"]
    """<p> The maximum expected bitrate (in bps) of the egress bridge.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddEgressGatewayBridgeRequest) -> dict:
    out: dict = {}
    if "max_bitrate" in value:
        out["maxBitrate"] = value["max_bitrate"]
    return out


def deserialize_json(data: dict) -> AddEgressGatewayBridgeRequest:
    out: AddEgressGatewayBridgeRequest = {}  # type: ignore[typeddict-item]
    if "maxBitrate" in data:
        out["max_bitrate"] = data["maxBitrate"]
    return out
