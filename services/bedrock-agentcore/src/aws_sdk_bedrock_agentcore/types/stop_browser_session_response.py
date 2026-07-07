"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#StopBrowserSessionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.browser_session_id
    import aws_sdk_bedrock_agentcore.types.date_timestamp


class StopBrowserSessionResponse(TypedDict, closed=True):
    browser_identifier: "str"
    """<p>The identifier of the browser.</p>"""
    session_id: "aws_sdk_bedrock_agentcore.types.browser_session_id.BrowserSessionId"
    """<p>The identifier of the browser session.</p>"""
    last_updated_at: "aws_sdk_bedrock_agentcore.types.date_timestamp.DateTimestamp"
    """<p>The time at which the browser session was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopBrowserSessionResponse) -> dict:
    out: dict = {}
    out["browserIdentifier"] = value["browser_identifier"]
    out["sessionId"] = value["session_id"]
    import aws_sdk_bedrock_agentcore.types.date_timestamp

    out["lastUpdatedAt"] = (
        aws_sdk_bedrock_agentcore.types.date_timestamp.serialize_json(
            value["last_updated_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> StopBrowserSessionResponse:
    out: StopBrowserSessionResponse = {}  # type: ignore[typeddict-item]
    if "browserIdentifier" in data:
        out["browser_identifier"] = data["browserIdentifier"]
    else:
        raise DeserializationError(
            "StopBrowserSessionResponse.browser_identifier required"
        )
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("StopBrowserSessionResponse.session_id required")
    if "lastUpdatedAt" in data:
        import aws_sdk_bedrock_agentcore.types.date_timestamp

        out["last_updated_at"] = (
            aws_sdk_bedrock_agentcore.types.date_timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    else:
        raise DeserializationError(
            "StopBrowserSessionResponse.last_updated_at required"
        )
    return out
