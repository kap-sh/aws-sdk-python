"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DescribeBridgeResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.bridge


class DescribeBridgeResponse(TypedDict):
    bridge: NotRequired["aws_sdk_mediaconnect.types.bridge.Bridge"]
    """<p>The bridge that you requested a description of. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeBridgeResponse) -> dict:
    out: dict = {}
    if "bridge" in value:
        import aws_sdk_mediaconnect.types.bridge

        out["bridge"] = aws_sdk_mediaconnect.types.bridge.serialize_json(
            value["bridge"]
        )
    return out


def deserialize_json(data: dict) -> DescribeBridgeResponse:
    out: DescribeBridgeResponse = {}  # type: ignore[typeddict-item]
    if "bridge" in data:
        import aws_sdk_mediaconnect.types.bridge

        out["bridge"] = aws_sdk_mediaconnect.types.bridge.deserialize_json(
            data["bridge"]
        )
    return out
