"""Generated from Smithy shape ``com.amazonaws.mediaconnect#UpdateIngressGatewayBridgeRequest``."""

from typing import TypedDict

from typing_extensions import NotRequired


class UpdateIngressGatewayBridgeRequest(TypedDict):
    max_bitrate: NotRequired["int"]
    """<p> The maximum expected bitrate (in bps).</p>"""
    max_outputs: NotRequired["int"]
    """<p> The maximum number of expected outputs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIngressGatewayBridgeRequest) -> dict:
    out: dict = {}
    if "max_bitrate" in value:
        out["maxBitrate"] = value["max_bitrate"]
    if "max_outputs" in value:
        out["maxOutputs"] = value["max_outputs"]
    return out


def deserialize_json(data: dict) -> UpdateIngressGatewayBridgeRequest:
    out: UpdateIngressGatewayBridgeRequest = {}  # type: ignore[typeddict-item]
    if "maxBitrate" in data:
        out["max_bitrate"] = data["maxBitrate"]
    if "maxOutputs" in data:
        out["max_outputs"] = data["maxOutputs"]
    return out
