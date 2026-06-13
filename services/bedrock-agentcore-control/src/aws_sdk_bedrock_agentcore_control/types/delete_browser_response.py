"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteBrowserResponse``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.browser_id
    import aws_sdk_bedrock_agentcore_control.types.browser_status
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp

class DeleteBrowserResponse(TypedDict):
    browser_id: "aws_sdk_bedrock_agentcore_control.types.browser_id.BrowserId"
    """<p>The unique identifier of the deleted browser.</p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.browser_status.BrowserStatus"
    """<p>The current status of the browser deletion.</p>"""
    last_updated_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the browser was last updated.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeleteBrowserResponse) -> dict:
    out: dict = {}
    out["browserId"] = value["browser_id"]
    import aws_sdk_bedrock_agentcore_control.types.browser_status
    out["status"] = aws_sdk_bedrock_agentcore_control.types.browser_status.serialize_json(value["status"])
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp
    out["lastUpdatedAt"] = aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(value["last_updated_at"])
    return out


def deserialize_json(data: dict) -> DeleteBrowserResponse:
    out: DeleteBrowserResponse = {}  # type: ignore[typeddict-item]
    if "browserId" in data:
        out["browser_id"] = data["browserId"]
    else:
        raise DeserializationError("DeleteBrowserResponse.browser_id required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.browser_status
        out["status"] = aws_sdk_bedrock_agentcore_control.types.browser_status.deserialize_json(data["status"])
    else:
        raise DeserializationError("DeleteBrowserResponse.status required")
    if "lastUpdatedAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp
        out["last_updated_at"] = aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(data["lastUpdatedAt"])
    else:
        raise DeserializationError("DeleteBrowserResponse.last_updated_at required")
    return out