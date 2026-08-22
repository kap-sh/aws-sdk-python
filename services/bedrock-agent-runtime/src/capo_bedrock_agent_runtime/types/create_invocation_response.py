"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#CreateInvocationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.date_timestamp
    import capo_bedrock_agent_runtime.types.uuid


class CreateInvocationResponse(TypedDict, closed=True):
    session_id: "capo_bedrock_agent_runtime.types.uuid.Uuid"
    """<p>The unique identifier for the session associated with the invocation.</p>"""
    invocation_id: "capo_bedrock_agent_runtime.types.uuid.Uuid"
    """<p>The unique identifier for the invocation.</p>"""
    created_at: "capo_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    """<p>The timestamp for when the invocation was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateInvocationResponse) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    out["invocationId"] = value["invocation_id"]
    import capo_bedrock_agent_runtime.types.date_timestamp

    out["createdAt"] = capo_bedrock_agent_runtime.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    return out


def deserialize_json(data: dict) -> CreateInvocationResponse:
    out: CreateInvocationResponse = {}  # type: ignore[typeddict-item]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("CreateInvocationResponse.session_id required")
    if data.get("invocationId") is not None:
        out["invocation_id"] = data["invocationId"]
    else:
        raise DeserializationError("CreateInvocationResponse.invocation_id required")
    if data.get("createdAt") is not None:
        import capo_bedrock_agent_runtime.types.date_timestamp

        out["created_at"] = (
            capo_bedrock_agent_runtime.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("CreateInvocationResponse.created_at required")
    return out
