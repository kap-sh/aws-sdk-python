"""Generated from Smithy shape ``com.amazonaws.mediaconnect#CreateBridgeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.bridge


class CreateBridgeResponse(TypedDict, closed=True):
    bridge: NotRequired["capo_mediaconnect.types.bridge.Bridge"]
    """<p> The name of the bridge that was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBridgeResponse) -> dict:
    out: dict = {}
    if "bridge" in value:
        import capo_mediaconnect.types.bridge

        out["bridge"] = capo_mediaconnect.types.bridge.serialize_json(value["bridge"])
    return out


def deserialize_json(data: dict) -> CreateBridgeResponse:
    out: CreateBridgeResponse = {}  # type: ignore[typeddict-item]
    if "bridge" in data:
        import capo_mediaconnect.types.bridge

        out["bridge"] = capo_mediaconnect.types.bridge.deserialize_json(data["bridge"])
    return out
