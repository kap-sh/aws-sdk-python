"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetBrowserSessionRequest``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.browser_session_id

class GetBrowserSessionRequest(TypedDict):
    browser_identifier: "str"
    """<p>The unique identifier of the browser associated with the session.</p>"""
    session_id: "aws_sdk_bedrock_agentcore.types.browser_session_id.BrowserSessionId"
    """<p>The unique identifier of the browser session to retrieve.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GetBrowserSessionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBrowserSessionRequest:
    out: GetBrowserSessionRequest = {}  # type: ignore[typeddict-item]
    return out