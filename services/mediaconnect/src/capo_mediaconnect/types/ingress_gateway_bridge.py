"""Generated from Smithy shape ``com.amazonaws.mediaconnect#IngressGatewayBridge``."""

from typing_extensions import NotRequired, TypedDict


class IngressGatewayBridge(TypedDict, closed=True):
    instance_id: NotRequired["str"]
    """<p>The ID of the instance running this bridge. </p>"""
    max_bitrate: NotRequired["int"]
    """<p>The maximum expected bitrate (in bps) of the ingress bridge. </p>"""
    max_outputs: NotRequired["int"]
    """<p>The maximum number of outputs on the ingress bridge. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IngressGatewayBridge) -> dict:
    out: dict = {}
    if "instance_id" in value:
        out["instanceId"] = value["instance_id"]
    if "max_bitrate" in value:
        out["maxBitrate"] = value["max_bitrate"]
    if "max_outputs" in value:
        out["maxOutputs"] = value["max_outputs"]
    return out


def deserialize_json(data: dict) -> IngressGatewayBridge:
    out: IngressGatewayBridge = {}  # type: ignore[typeddict-item]
    if "instanceId" in data:
        out["instance_id"] = data["instanceId"]
    if "maxBitrate" in data:
        out["max_bitrate"] = data["maxBitrate"]
    if "maxOutputs" in data:
        out["max_outputs"] = data["maxOutputs"]
    return out
