"""Generated from Smithy shape ``com.amazonaws.mediaconnect#UpdateBridgeOutputResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.bridge_output


class UpdateBridgeOutputResponse(TypedDict, closed=True):
    bridge_arn: NotRequired["str"]
    """<p> The ARN of the bridge that was updated. </p>"""
    output: NotRequired["capo_mediaconnect.types.bridge_output.BridgeOutput"]
    """<p> The bridge output that was updated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBridgeOutputResponse) -> dict:
    out: dict = {}
    if "bridge_arn" in value:
        out["bridgeArn"] = value["bridge_arn"]
    if "output" in value:
        import capo_mediaconnect.types.bridge_output

        out["output"] = capo_mediaconnect.types.bridge_output.serialize_json(
            value["output"]
        )
    return out


def deserialize_json(data: dict) -> UpdateBridgeOutputResponse:
    out: UpdateBridgeOutputResponse = {}  # type: ignore[typeddict-item]
    if "bridgeArn" in data:
        out["bridge_arn"] = data["bridgeArn"]
    if "output" in data:
        import capo_mediaconnect.types.bridge_output

        out["output"] = capo_mediaconnect.types.bridge_output.deserialize_json(
            data["output"]
        )
    return out
