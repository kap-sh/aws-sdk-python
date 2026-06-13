"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateBrowserResponse``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.browser_arn
    import aws_sdk_bedrock_agentcore_control.types.browser_id
    import aws_sdk_bedrock_agentcore_control.types.browser_status
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp

class CreateBrowserResponse(TypedDict):
    browser_id: "aws_sdk_bedrock_agentcore_control.types.browser_id.BrowserId"
    """<p>The unique identifier of the created browser.</p>"""
    browser_arn: "aws_sdk_bedrock_agentcore_control.types.browser_arn.BrowserArn"
    """<p>The Amazon Resource Name (ARN) of the created browser.</p>"""
    created_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the browser was created.</p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.browser_status.BrowserStatus"
    """<p>The current status of the browser.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateBrowserResponse) -> dict:
    out: dict = {}
    out["browserId"] = value["browser_id"]
    out["browserArn"] = value["browser_arn"]
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp
    out["createdAt"] = aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(value["created_at"])
    import aws_sdk_bedrock_agentcore_control.types.browser_status
    out["status"] = aws_sdk_bedrock_agentcore_control.types.browser_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> CreateBrowserResponse:
    out: CreateBrowserResponse = {}  # type: ignore[typeddict-item]
    if "browserId" in data:
        out["browser_id"] = data["browserId"]
    else:
        raise DeserializationError("CreateBrowserResponse.browser_id required")
    if "browserArn" in data:
        out["browser_arn"] = data["browserArn"]
    else:
        raise DeserializationError("CreateBrowserResponse.browser_arn required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp
        out["created_at"] = aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(data["createdAt"])
    else:
        raise DeserializationError("CreateBrowserResponse.created_at required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.browser_status
        out["status"] = aws_sdk_bedrock_agentcore_control.types.browser_status.deserialize_json(data["status"])
    else:
        raise DeserializationError("CreateBrowserResponse.status required")
    return out