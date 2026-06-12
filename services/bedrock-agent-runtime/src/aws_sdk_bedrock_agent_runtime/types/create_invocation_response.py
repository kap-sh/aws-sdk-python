"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#CreateInvocationResponse``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock_agent_runtime.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.date_timestamp
    import aws_sdk_bedrock_agent_runtime.types.uuid

class CreateInvocationResponse(TypedDict):
    session_id: "aws_sdk_bedrock_agent_runtime.types.uuid.Uuid"
    """<p>The unique identifier for the session associated with the invocation.</p>"""
    invocation_id: "aws_sdk_bedrock_agent_runtime.types.uuid.Uuid"
    """<p>The unique identifier for the invocation.</p>"""
    created_at: "aws_sdk_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    """<p>The timestamp for when the invocation was created.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateInvocationResponse) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    out["invocationId"] = value["invocation_id"]
    import aws_sdk_bedrock_agent_runtime.types.date_timestamp
    out["createdAt"] = aws_sdk_bedrock_agent_runtime.types.date_timestamp.serialize_json(value["created_at"])
    return out


def deserialize_json(data: dict) -> CreateInvocationResponse:
    out: CreateInvocationResponse = {}  # type: ignore[typeddict-item]
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("CreateInvocationResponse.session_id required")
    if "invocationId" in data:
        out["invocation_id"] = data["invocationId"]
    else:
        raise DeserializationError("CreateInvocationResponse.invocation_id required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agent_runtime.types.date_timestamp
        out["created_at"] = aws_sdk_bedrock_agent_runtime.types.date_timestamp.deserialize_json(data["createdAt"])
    else:
        raise DeserializationError("CreateInvocationResponse.created_at required")
    return out