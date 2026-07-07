"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#StopBrowserSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.browser_session_id
    import aws_sdk_bedrock_agentcore.types.client_token


class StopBrowserSessionRequest(TypedDict, closed=True):
    trace_id: NotRequired["str"]
    """<p>The trace identifier for request tracking.</p>"""
    trace_parent: NotRequired["str"]
    """<p>The parent trace information for distributed tracing.</p>"""
    browser_identifier: "str"
    """<p>The unique identifier of the browser associated with the session.</p>"""
    session_id: "aws_sdk_bedrock_agentcore.types.browser_session_id.BrowserSessionId"
    """<p>The unique identifier of the browser session to stop.</p>"""
    client_token: NotRequired[
        "aws_sdk_bedrock_agentcore.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request, but does not return an error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopBrowserSessionRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> StopBrowserSessionRequest:
    out: StopBrowserSessionRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
