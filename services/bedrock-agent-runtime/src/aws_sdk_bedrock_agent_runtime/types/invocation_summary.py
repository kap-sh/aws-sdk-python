"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InvocationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.date_timestamp
    import aws_sdk_bedrock_agent_runtime.types.uuid


class InvocationSummary(TypedDict, closed=True):
    session_id: "aws_sdk_bedrock_agent_runtime.types.uuid.Uuid"
    """<p>The unique identifier for the session associated with the invocation.</p>"""
    invocation_id: "aws_sdk_bedrock_agent_runtime.types.uuid.Uuid"
    """<p>A unique identifier for the invocation in UUID format.</p>"""
    created_at: "aws_sdk_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    """<p>The timestamp for when the invocation was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvocationSummary) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    out["invocationId"] = value["invocation_id"]
    import aws_sdk_bedrock_agent_runtime.types.date_timestamp

    out["createdAt"] = (
        aws_sdk_bedrock_agent_runtime.types.date_timestamp.serialize_json(
            value["created_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> InvocationSummary:
    out: InvocationSummary = {}  # type: ignore[typeddict-item]
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("InvocationSummary.session_id required")
    if "invocationId" in data:
        out["invocation_id"] = data["invocationId"]
    else:
        raise DeserializationError("InvocationSummary.invocation_id required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agent_runtime.types.date_timestamp

        out["created_at"] = (
            aws_sdk_bedrock_agent_runtime.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("InvocationSummary.created_at required")
    return out
