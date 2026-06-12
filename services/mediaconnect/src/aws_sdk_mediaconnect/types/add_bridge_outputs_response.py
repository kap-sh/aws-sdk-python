"""Generated from Smithy shape ``com.amazonaws.mediaconnect#AddBridgeOutputsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__list_of_bridge_output

class AddBridgeOutputsResponse(TypedDict):
    bridge_arn: NotRequired["str"]
    """<p> The ARN of the bridge that you added outputs to.</p>"""
    outputs: NotRequired["aws_sdk_mediaconnect.types.__list_of_bridge_output.__listOfBridgeOutput"]
    """<p> The outputs that you added to this bridge.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AddBridgeOutputsResponse) -> dict:
    out: dict = {}
    if "bridge_arn" in value:
        out["bridgeArn"] = value["bridge_arn"]
    if "outputs" in value:
        import aws_sdk_mediaconnect.types.__list_of_bridge_output
        out["outputs"] = aws_sdk_mediaconnect.types.__list_of_bridge_output.serialize_json(value["outputs"])
    return out


def deserialize_json(data: dict) -> AddBridgeOutputsResponse:
    out: AddBridgeOutputsResponse = {}  # type: ignore[typeddict-item]
    if "bridgeArn" in data:
        out["bridge_arn"] = data["bridgeArn"]
    if "outputs" in data:
        import aws_sdk_mediaconnect.types.__list_of_bridge_output
        out["outputs"] = aws_sdk_mediaconnect.types.__list_of_bridge_output.deserialize_json(data["outputs"])
    return out