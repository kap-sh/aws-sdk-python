"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DeleteBridgeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.bridge_arn


class DeleteBridgeRequest(TypedDict, closed=True):
    bridge_arn: "capo_mediaconnect.types.bridge_arn.BridgeArn"
    """<p> The Amazon Resource Name (ARN) of the bridge that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBridgeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteBridgeRequest:
    out: DeleteBridgeRequest = {}  # type: ignore[typeddict-item]
    return out
