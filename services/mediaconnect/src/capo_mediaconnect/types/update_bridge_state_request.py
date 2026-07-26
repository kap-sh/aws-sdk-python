"""Generated from Smithy shape ``com.amazonaws.mediaconnect#UpdateBridgeStateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.bridge_arn
    import capo_mediaconnect.types.desired_state


class UpdateBridgeStateRequest(TypedDict, closed=True):
    bridge_arn: "capo_mediaconnect.types.bridge_arn.BridgeArn"
    """<p> The Amazon Resource Name (ARN) of the bridge that you want to update the state of. </p>"""
    desired_state: NotRequired["capo_mediaconnect.types.desired_state.DesiredState"]
    """<p> The desired state for the bridge. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBridgeStateRequest) -> dict:
    out: dict = {}
    if "desired_state" in value:
        import capo_mediaconnect.types.desired_state

        out["desiredState"] = capo_mediaconnect.types.desired_state.serialize_json(
            value["desired_state"]
        )
    return out


def deserialize_json(data: dict) -> UpdateBridgeStateRequest:
    out: UpdateBridgeStateRequest = {}  # type: ignore[typeddict-item]
    if "desiredState" in data:
        import capo_mediaconnect.types.desired_state

        out["desired_state"] = capo_mediaconnect.types.desired_state.deserialize_json(
            data["desiredState"]
        )
    return out
