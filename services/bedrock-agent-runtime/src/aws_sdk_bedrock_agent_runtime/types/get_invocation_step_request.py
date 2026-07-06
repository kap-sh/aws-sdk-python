"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GetInvocationStepRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.invocation_identifier
    import aws_sdk_bedrock_agent_runtime.types.session_identifier
    import aws_sdk_bedrock_agent_runtime.types.uuid


class GetInvocationStepRequest(TypedDict, closed=True):
    invocation_identifier: (
        "aws_sdk_bedrock_agent_runtime.types.invocation_identifier.InvocationIdentifier"
    )
    """<p>The unique identifier for the invocation in UUID format.</p>"""
    invocation_step_id: "aws_sdk_bedrock_agent_runtime.types.uuid.Uuid"
    """<p>The unique identifier (in UUID format) for the specific invocation step to retrieve.</p>"""
    session_identifier: (
        "aws_sdk_bedrock_agent_runtime.types.session_identifier.SessionIdentifier"
    )
    """<p>The unique identifier for the invocation step's associated session. You can specify either the session's <code>sessionId</code> or its Amazon Resource Name (ARN).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInvocationStepRequest) -> dict:
    out: dict = {}
    out["invocationIdentifier"] = value["invocation_identifier"]
    return out


def deserialize_json(data: dict) -> GetInvocationStepRequest:
    out: GetInvocationStepRequest = {}  # type: ignore[typeddict-item]
    if "invocationIdentifier" in data:
        out["invocation_identifier"] = data["invocationIdentifier"]
    else:
        raise DeserializationError(
            "GetInvocationStepRequest.invocation_identifier required"
        )
    return out
