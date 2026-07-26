"""Generated from Smithy shape ``com.amazonaws.mediaconnect#UpdateEgressGatewayBridgeRequest``."""

from typing_extensions import NotRequired, TypedDict


class UpdateEgressGatewayBridgeRequest(TypedDict, closed=True):
    max_bitrate: NotRequired["int"]
    """<p>The maximum expected bitrate (in bps). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEgressGatewayBridgeRequest) -> dict:
    out: dict = {}
    if "max_bitrate" in value:
        out["maxBitrate"] = value["max_bitrate"]
    return out


def deserialize_json(data: dict) -> UpdateEgressGatewayBridgeRequest:
    out: UpdateEgressGatewayBridgeRequest = {}  # type: ignore[typeddict-item]
    if "maxBitrate" in data:
        out["max_bitrate"] = data["maxBitrate"]
    return out
