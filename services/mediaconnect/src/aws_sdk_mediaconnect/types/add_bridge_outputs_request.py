"""Generated from Smithy shape ``com.amazonaws.mediaconnect#AddBridgeOutputsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__list_of_add_bridge_output_request
    import aws_sdk_mediaconnect.types.bridge_arn

class AddBridgeOutputsRequest(TypedDict):
    bridge_arn: "aws_sdk_mediaconnect.types.bridge_arn.BridgeArn"
    """<p> The Amazon Resource Name (ARN) of the bridge that you want to update.</p>"""
    outputs: NotRequired["aws_sdk_mediaconnect.types.__list_of_add_bridge_output_request.__listOfAddBridgeOutputRequest"]
    """<p> The outputs that you want to add to this bridge.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AddBridgeOutputsRequest) -> dict:
    out: dict = {}
    if "outputs" in value:
        import aws_sdk_mediaconnect.types.__list_of_add_bridge_output_request
        out["outputs"] = aws_sdk_mediaconnect.types.__list_of_add_bridge_output_request.serialize_json(value["outputs"])
    return out


def deserialize_json(data: dict) -> AddBridgeOutputsRequest:
    out: AddBridgeOutputsRequest = {}  # type: ignore[typeddict-item]
    if "outputs" in data:
        import aws_sdk_mediaconnect.types.__list_of_add_bridge_output_request
        out["outputs"] = aws_sdk_mediaconnect.types.__list_of_add_bridge_output_request.deserialize_json(data["outputs"])
    return out