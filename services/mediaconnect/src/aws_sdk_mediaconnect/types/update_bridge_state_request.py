"""Generated from Smithy shape ``com.amazonaws.mediaconnect#UpdateBridgeStateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.bridge_arn
    import aws_sdk_mediaconnect.types.desired_state


class UpdateBridgeStateRequest(TypedDict):
    bridge_arn: "aws_sdk_mediaconnect.types.bridge_arn.BridgeArn"
    """<p> The Amazon Resource Name (ARN) of the bridge that you want to update the state of. </p>"""
    desired_state: NotRequired["aws_sdk_mediaconnect.types.desired_state.DesiredState"]
    """<p> The desired state for the bridge. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBridgeStateRequest) -> dict:
    out: dict = {}
    if "desired_state" in value:
        import aws_sdk_mediaconnect.types.desired_state

        out["desiredState"] = aws_sdk_mediaconnect.types.desired_state.serialize_json(
            value["desired_state"]
        )
    return out


def deserialize_json(data: dict) -> UpdateBridgeStateRequest:
    out: UpdateBridgeStateRequest = {}  # type: ignore[typeddict-item]
    if "desiredState" in data:
        import aws_sdk_mediaconnect.types.desired_state

        out["desired_state"] = (
            aws_sdk_mediaconnect.types.desired_state.deserialize_json(
                data["desiredState"]
            )
        )
    return out
