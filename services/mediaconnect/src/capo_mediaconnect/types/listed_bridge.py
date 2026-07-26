"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ListedBridge``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.bridge_state


class ListedBridge(TypedDict, closed=True):
    bridge_arn: NotRequired["str"]
    """<p> The ARN of the bridge.</p>"""
    bridge_state: NotRequired["capo_mediaconnect.types.bridge_state.BridgeState"]
    """<p>The state of the bridge. </p>"""
    bridge_type: NotRequired["str"]
    """<p> The type of the bridge.</p>"""
    name: NotRequired["str"]
    """<p> The name of the bridge.</p>"""
    placement_arn: NotRequired["str"]
    """<p> The ARN of the gateway associated with the bridge.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListedBridge) -> dict:
    out: dict = {}
    if "bridge_arn" in value:
        out["bridgeArn"] = value["bridge_arn"]
    if "bridge_state" in value:
        import capo_mediaconnect.types.bridge_state

        out["bridgeState"] = capo_mediaconnect.types.bridge_state.serialize_json(
            value["bridge_state"]
        )
    if "bridge_type" in value:
        out["bridgeType"] = value["bridge_type"]
    if "name" in value:
        out["name"] = value["name"]
    if "placement_arn" in value:
        out["placementArn"] = value["placement_arn"]
    return out


def deserialize_json(data: dict) -> ListedBridge:
    out: ListedBridge = {}  # type: ignore[typeddict-item]
    if "bridgeArn" in data:
        out["bridge_arn"] = data["bridgeArn"]
    if "bridgeState" in data:
        import capo_mediaconnect.types.bridge_state

        out["bridge_state"] = capo_mediaconnect.types.bridge_state.deserialize_json(
            data["bridgeState"]
        )
    if "bridgeType" in data:
        out["bridge_type"] = data["bridgeType"]
    if "name" in data:
        out["name"] = data["name"]
    if "placementArn" in data:
        out["placement_arn"] = data["placementArn"]
    return out
