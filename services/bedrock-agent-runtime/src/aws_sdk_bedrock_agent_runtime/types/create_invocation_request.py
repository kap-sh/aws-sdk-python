"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#CreateInvocationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.invocation_description
    import aws_sdk_bedrock_agent_runtime.types.session_identifier
    import aws_sdk_bedrock_agent_runtime.types.uuid

class CreateInvocationRequest(TypedDict):
    invocation_id: NotRequired["aws_sdk_bedrock_agent_runtime.types.uuid.Uuid"]
    """<p>A unique identifier for the invocation in UUID format.</p>"""
    description: NotRequired["aws_sdk_bedrock_agent_runtime.types.invocation_description.InvocationDescription"]
    """<p>A description for the interactions in the invocation. For example, \"User asking about weather in Seattle\".</p>"""
    session_identifier: "aws_sdk_bedrock_agent_runtime.types.session_identifier.SessionIdentifier"
    """<p>The unique identifier for the associated session for the invocation. You can specify either the session's <code>sessionId</code> or its Amazon Resource Name (ARN). </p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateInvocationRequest) -> dict:
    out: dict = {}
    if "invocation_id" in value:
        out["invocationId"] = value["invocation_id"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> CreateInvocationRequest:
    out: CreateInvocationRequest = {}  # type: ignore[typeddict-item]
    if "invocationId" in data:
        out["invocation_id"] = data["invocationId"]
    if "description" in data:
        out["description"] = data["description"]
    return out