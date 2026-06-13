"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RemoveBridgeOutputResponse``."""

from typing import TypedDict

from typing_extensions import NotRequired


class RemoveBridgeOutputResponse(TypedDict):
    bridge_arn: NotRequired["str"]
    """<p> The ARN of the bridge from which the output was removed. </p>"""
    output_name: NotRequired["str"]
    """<p> The name of the bridge output that was removed. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveBridgeOutputResponse) -> dict:
    out: dict = {}
    if "bridge_arn" in value:
        out["bridgeArn"] = value["bridge_arn"]
    if "output_name" in value:
        out["outputName"] = value["output_name"]
    return out


def deserialize_json(data: dict) -> RemoveBridgeOutputResponse:
    out: RemoveBridgeOutputResponse = {}  # type: ignore[typeddict-item]
    if "bridgeArn" in data:
        out["bridge_arn"] = data["bridgeArn"]
    if "outputName" in data:
        out["output_name"] = data["outputName"]
    return out
