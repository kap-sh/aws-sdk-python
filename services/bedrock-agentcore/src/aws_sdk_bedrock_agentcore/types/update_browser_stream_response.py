"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#UpdateBrowserStreamResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.browser_session_id
    import aws_sdk_bedrock_agentcore.types.browser_session_stream
    import aws_sdk_bedrock_agentcore.types.date_timestamp


class UpdateBrowserStreamResponse(TypedDict):
    browser_identifier: "str"
    """<p>The identifier of the browser.</p>"""
    session_id: "aws_sdk_bedrock_agentcore.types.browser_session_id.BrowserSessionId"
    """<p>The identifier of the browser session.</p>"""
    streams: (
        "aws_sdk_bedrock_agentcore.types.browser_session_stream.BrowserSessionStream"
    )
    updated_at: "aws_sdk_bedrock_agentcore.types.date_timestamp.DateTimestamp"
    """<p>The time at which the browser stream was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBrowserStreamResponse) -> dict:
    out: dict = {}
    out["browserIdentifier"] = value["browser_identifier"]
    out["sessionId"] = value["session_id"]
    import aws_sdk_bedrock_agentcore.types.browser_session_stream

    out["streams"] = (
        aws_sdk_bedrock_agentcore.types.browser_session_stream.serialize_json(
            value["streams"]
        )
    )
    import aws_sdk_bedrock_agentcore.types.date_timestamp

    out["updatedAt"] = aws_sdk_bedrock_agentcore.types.date_timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> UpdateBrowserStreamResponse:
    out: UpdateBrowserStreamResponse = {}  # type: ignore[typeddict-item]
    if "browserIdentifier" in data:
        out["browser_identifier"] = data["browserIdentifier"]
    else:
        raise DeserializationError(
            "UpdateBrowserStreamResponse.browser_identifier required"
        )
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("UpdateBrowserStreamResponse.session_id required")
    if "streams" in data:
        import aws_sdk_bedrock_agentcore.types.browser_session_stream

        out["streams"] = (
            aws_sdk_bedrock_agentcore.types.browser_session_stream.deserialize_json(
                data["streams"]
            )
        )
    else:
        raise DeserializationError("UpdateBrowserStreamResponse.streams required")
    if "updatedAt" in data:
        import aws_sdk_bedrock_agentcore.types.date_timestamp

        out["updated_at"] = (
            aws_sdk_bedrock_agentcore.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("UpdateBrowserStreamResponse.updated_at required")
    return out
