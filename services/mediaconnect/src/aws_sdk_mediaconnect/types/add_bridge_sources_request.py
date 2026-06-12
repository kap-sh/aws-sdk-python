"""Generated from Smithy shape ``com.amazonaws.mediaconnect#AddBridgeSourcesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__list_of_add_bridge_source_request
    import aws_sdk_mediaconnect.types.bridge_arn

class AddBridgeSourcesRequest(TypedDict):
    bridge_arn: "aws_sdk_mediaconnect.types.bridge_arn.BridgeArn"
    """<p> The Amazon Resource Name (ARN) of the bridge that you want to update.</p>"""
    sources: NotRequired["aws_sdk_mediaconnect.types.__list_of_add_bridge_source_request.__listOfAddBridgeSourceRequest"]
    """<p> The sources that you want to add to this bridge.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AddBridgeSourcesRequest) -> dict:
    out: dict = {}
    if "sources" in value:
        import aws_sdk_mediaconnect.types.__list_of_add_bridge_source_request
        out["sources"] = aws_sdk_mediaconnect.types.__list_of_add_bridge_source_request.serialize_json(value["sources"])
    return out


def deserialize_json(data: dict) -> AddBridgeSourcesRequest:
    out: AddBridgeSourcesRequest = {}  # type: ignore[typeddict-item]
    if "sources" in data:
        import aws_sdk_mediaconnect.types.__list_of_add_bridge_source_request
        out["sources"] = aws_sdk_mediaconnect.types.__list_of_add_bridge_source_request.deserialize_json(data["sources"])
    return out