"""Generated from Smithy shape ``com.amazonaws.mediaconnect#UpdateBridgeResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.bridge


class UpdateBridgeResponse(TypedDict):
    bridge: NotRequired["aws_sdk_mediaconnect.types.bridge.Bridge"]
    """<p> The bridge that was updated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBridgeResponse) -> dict:
    out: dict = {}
    if "bridge" in value:
        import aws_sdk_mediaconnect.types.bridge

        out["bridge"] = aws_sdk_mediaconnect.types.bridge.serialize_json(
            value["bridge"]
        )
    return out


def deserialize_json(data: dict) -> UpdateBridgeResponse:
    out: UpdateBridgeResponse = {}  # type: ignore[typeddict-item]
    if "bridge" in data:
        import aws_sdk_mediaconnect.types.bridge

        out["bridge"] = aws_sdk_mediaconnect.types.bridge.deserialize_json(
            data["bridge"]
        )
    return out
