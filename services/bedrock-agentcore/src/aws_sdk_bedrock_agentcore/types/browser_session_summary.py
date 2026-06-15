"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BrowserSessionSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.browser_session_id
    import aws_sdk_bedrock_agentcore.types.browser_session_status
    import aws_sdk_bedrock_agentcore.types.date_timestamp
    import aws_sdk_bedrock_agentcore.types.name


class BrowserSessionSummary(TypedDict):
    browser_identifier: "str"
    """<p>The unique identifier of the browser associated with the session. This identifier specifies which browser environment is used for the session.</p>"""
    session_id: "aws_sdk_bedrock_agentcore.types.browser_session_id.BrowserSessionId"
    """<p>The unique identifier of the browser session. This identifier is used in operations that interact with the session.</p>"""
    name: NotRequired["aws_sdk_bedrock_agentcore.types.name.Name"]
    """<p>The name of the browser session. This name helps identify and manage the session.</p>"""
    status: (
        "aws_sdk_bedrock_agentcore.types.browser_session_status.BrowserSessionStatus"
    )
    """<p>The current status of the browser session. Possible values include ACTIVE, STOPPING, and STOPPED.</p>"""
    created_at: "aws_sdk_bedrock_agentcore.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the browser session was created. This value is in ISO 8601 format.</p>"""
    last_updated_at: NotRequired[
        "aws_sdk_bedrock_agentcore.types.date_timestamp.DateTimestamp"
    ]
    """<p>The timestamp when the browser session was last updated. This value is in ISO 8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BrowserSessionSummary) -> dict:
    out: dict = {}
    out["browserIdentifier"] = value["browser_identifier"]
    out["sessionId"] = value["session_id"]
    if "name" in value:
        out["name"] = value["name"]
    import aws_sdk_bedrock_agentcore.types.browser_session_status

    out["status"] = (
        aws_sdk_bedrock_agentcore.types.browser_session_status.serialize_json(
            value["status"]
        )
    )
    import aws_sdk_bedrock_agentcore.types.date_timestamp

    out["createdAt"] = aws_sdk_bedrock_agentcore.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    if "last_updated_at" in value:
        import aws_sdk_bedrock_agentcore.types.date_timestamp

        out["lastUpdatedAt"] = (
            aws_sdk_bedrock_agentcore.types.date_timestamp.serialize_json(
                value["last_updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> BrowserSessionSummary:
    out: BrowserSessionSummary = {}  # type: ignore[typeddict-item]
    if "browserIdentifier" in data:
        out["browser_identifier"] = data["browserIdentifier"]
    else:
        raise DeserializationError("BrowserSessionSummary.browser_identifier required")
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("BrowserSessionSummary.session_id required")
    if "name" in data:
        out["name"] = data["name"]
    if "status" in data:
        import aws_sdk_bedrock_agentcore.types.browser_session_status

        out["status"] = (
            aws_sdk_bedrock_agentcore.types.browser_session_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("BrowserSessionSummary.status required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore.types.date_timestamp

        out["created_at"] = (
            aws_sdk_bedrock_agentcore.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("BrowserSessionSummary.created_at required")
    if "lastUpdatedAt" in data:
        import aws_sdk_bedrock_agentcore.types.date_timestamp

        out["last_updated_at"] = (
            aws_sdk_bedrock_agentcore.types.date_timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    return out
