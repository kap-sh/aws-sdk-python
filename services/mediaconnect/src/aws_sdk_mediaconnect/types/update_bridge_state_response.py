"""Generated from Smithy shape ``com.amazonaws.mediaconnect#UpdateBridgeStateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.desired_state


class UpdateBridgeStateResponse(TypedDict, closed=True):
    bridge_arn: NotRequired["str"]
    """<p>The ARN of the updated bridge. </p>"""
    desired_state: NotRequired["aws_sdk_mediaconnect.types.desired_state.DesiredState"]
    """<p> The new state of the bridge. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBridgeStateResponse) -> dict:
    out: dict = {}
    if "bridge_arn" in value:
        out["bridgeArn"] = value["bridge_arn"]
    if "desired_state" in value:
        import aws_sdk_mediaconnect.types.desired_state

        out["desiredState"] = aws_sdk_mediaconnect.types.desired_state.serialize_json(
            value["desired_state"]
        )
    return out


def deserialize_json(data: dict) -> UpdateBridgeStateResponse:
    out: UpdateBridgeStateResponse = {}  # type: ignore[typeddict-item]
    if "bridgeArn" in data:
        out["bridge_arn"] = data["bridgeArn"]
    if "desiredState" in data:
        import aws_sdk_mediaconnect.types.desired_state

        out["desired_state"] = (
            aws_sdk_mediaconnect.types.desired_state.deserialize_json(
                data["desiredState"]
            )
        )
    return out
