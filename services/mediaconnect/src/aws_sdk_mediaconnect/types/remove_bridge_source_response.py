"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RemoveBridgeSourceResponse``."""

from typing_extensions import NotRequired, TypedDict


class RemoveBridgeSourceResponse(TypedDict, closed=True):
    bridge_arn: NotRequired["str"]
    """<p> The ARN of the bridge from which the source was removed. </p>"""
    source_name: NotRequired["str"]
    """<p> The name of the bridge source that was removed. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveBridgeSourceResponse) -> dict:
    out: dict = {}
    if "bridge_arn" in value:
        out["bridgeArn"] = value["bridge_arn"]
    if "source_name" in value:
        out["sourceName"] = value["source_name"]
    return out


def deserialize_json(data: dict) -> RemoveBridgeSourceResponse:
    out: RemoveBridgeSourceResponse = {}  # type: ignore[typeddict-item]
    if "bridgeArn" in data:
        out["bridge_arn"] = data["bridgeArn"]
    if "sourceName" in data:
        out["source_name"] = data["sourceName"]
    return out
