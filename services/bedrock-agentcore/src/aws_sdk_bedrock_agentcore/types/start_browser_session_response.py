"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#StartBrowserSessionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.browser_session_id
    import aws_sdk_bedrock_agentcore.types.browser_session_stream
    import aws_sdk_bedrock_agentcore.types.date_timestamp


class StartBrowserSessionResponse(TypedDict):
    browser_identifier: "str"
    """<p>The identifier of the browser.</p>"""
    session_id: "aws_sdk_bedrock_agentcore.types.browser_session_id.BrowserSessionId"
    """<p>The unique identifier of the created browser session.</p>"""
    created_at: "aws_sdk_bedrock_agentcore.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the browser session was created.</p>"""
    streams: NotRequired[
        "aws_sdk_bedrock_agentcore.types.browser_session_stream.BrowserSessionStream"
    ]
    """<p>The streams associated with this browser session. These include the automation stream and live view stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartBrowserSessionResponse) -> dict:
    out: dict = {}
    out["browserIdentifier"] = value["browser_identifier"]
    out["sessionId"] = value["session_id"]
    import aws_sdk_bedrock_agentcore.types.date_timestamp

    out["createdAt"] = aws_sdk_bedrock_agentcore.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    if "streams" in value:
        import aws_sdk_bedrock_agentcore.types.browser_session_stream

        out["streams"] = (
            aws_sdk_bedrock_agentcore.types.browser_session_stream.serialize_json(
                value["streams"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartBrowserSessionResponse:
    out: StartBrowserSessionResponse = {}  # type: ignore[typeddict-item]
    if "browserIdentifier" in data:
        out["browser_identifier"] = data["browserIdentifier"]
    else:
        raise DeserializationError(
            "StartBrowserSessionResponse.browser_identifier required"
        )
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("StartBrowserSessionResponse.session_id required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore.types.date_timestamp

        out["created_at"] = (
            aws_sdk_bedrock_agentcore.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("StartBrowserSessionResponse.created_at required")
    if "streams" in data:
        import aws_sdk_bedrock_agentcore.types.browser_session_stream

        out["streams"] = (
            aws_sdk_bedrock_agentcore.types.browser_session_stream.deserialize_json(
                data["streams"]
            )
        )
    return out
