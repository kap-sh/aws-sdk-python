"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DeleteBridgeResponse``."""

from typing import TypedDict
from typing_extensions import NotRequired

class DeleteBridgeResponse(TypedDict):
    bridge_arn: NotRequired["str"]
    """<p> The ARN of the deleted bridge.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeleteBridgeResponse) -> dict:
    out: dict = {}
    if "bridge_arn" in value:
        out["bridgeArn"] = value["bridge_arn"]
    return out


def deserialize_json(data: dict) -> DeleteBridgeResponse:
    out: DeleteBridgeResponse = {}  # type: ignore[typeddict-item]
    if "bridgeArn" in data:
        out["bridge_arn"] = data["bridgeArn"]
    return out