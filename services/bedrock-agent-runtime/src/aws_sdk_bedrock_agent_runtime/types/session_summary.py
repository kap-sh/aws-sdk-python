"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#SessionSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.date_timestamp
    import aws_sdk_bedrock_agent_runtime.types.session_arn
    import aws_sdk_bedrock_agent_runtime.types.session_status
    import aws_sdk_bedrock_agent_runtime.types.uuid


class SessionSummary(TypedDict):
    session_id: "aws_sdk_bedrock_agent_runtime.types.uuid.Uuid"
    """<p>The unique identifier for the session.</p>"""
    session_arn: "aws_sdk_bedrock_agent_runtime.types.session_arn.SessionArn"
    """<p>The Amazon Resource Name (ARN) of the session.</p>"""
    session_status: "aws_sdk_bedrock_agent_runtime.types.session_status.SessionStatus"
    """<p>The current status of the session.</p>"""
    created_at: "aws_sdk_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    """<p>The timestamp for when the session was created.</p>"""
    last_updated_at: "aws_sdk_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    """<p>The timestamp for when the session was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionSummary) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    out["sessionArn"] = value["session_arn"]
    import aws_sdk_bedrock_agent_runtime.types.session_status

    out["sessionStatus"] = (
        aws_sdk_bedrock_agent_runtime.types.session_status.serialize_json(
            value["session_status"]
        )
    )
    import aws_sdk_bedrock_agent_runtime.types.date_timestamp

    out["createdAt"] = (
        aws_sdk_bedrock_agent_runtime.types.date_timestamp.serialize_json(
            value["created_at"]
        )
    )
    import aws_sdk_bedrock_agent_runtime.types.date_timestamp

    out["lastUpdatedAt"] = (
        aws_sdk_bedrock_agent_runtime.types.date_timestamp.serialize_json(
            value["last_updated_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> SessionSummary:
    out: SessionSummary = {}  # type: ignore[typeddict-item]
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("SessionSummary.session_id required")
    if "sessionArn" in data:
        out["session_arn"] = data["sessionArn"]
    else:
        raise DeserializationError("SessionSummary.session_arn required")
    if "sessionStatus" in data:
        import aws_sdk_bedrock_agent_runtime.types.session_status

        out["session_status"] = (
            aws_sdk_bedrock_agent_runtime.types.session_status.deserialize_json(
                data["sessionStatus"]
            )
        )
    else:
        raise DeserializationError("SessionSummary.session_status required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agent_runtime.types.date_timestamp

        out["created_at"] = (
            aws_sdk_bedrock_agent_runtime.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("SessionSummary.created_at required")
    if "lastUpdatedAt" in data:
        import aws_sdk_bedrock_agent_runtime.types.date_timestamp

        out["last_updated_at"] = (
            aws_sdk_bedrock_agent_runtime.types.date_timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    else:
        raise DeserializationError("SessionSummary.last_updated_at required")
    return out
