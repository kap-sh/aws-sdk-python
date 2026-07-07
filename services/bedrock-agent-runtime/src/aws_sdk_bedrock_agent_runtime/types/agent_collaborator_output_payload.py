"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgentCollaboratorOutputPayload``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.agent_collaborator_payload_string
    import aws_sdk_bedrock_agent_runtime.types.payload_type
    import aws_sdk_bedrock_agent_runtime.types.return_control_payload


class AgentCollaboratorOutputPayload(TypedDict, closed=True):
    type: NotRequired["aws_sdk_bedrock_agent_runtime.types.payload_type.PayloadType"]
    """<p>The type of output.</p>"""
    text: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.agent_collaborator_payload_string.AgentCollaboratorPayloadString"
    ]
    """<p>Text output.</p>"""
    return_control_payload: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.return_control_payload.ReturnControlPayload"
    ]
    """<p>An action invocation result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentCollaboratorOutputPayload) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_bedrock_agent_runtime.types.payload_type

        out["type"] = aws_sdk_bedrock_agent_runtime.types.payload_type.serialize_json(
            value["type"]
        )
    if "text" in value:
        out["text"] = value["text"]
    if "return_control_payload" in value:
        import aws_sdk_bedrock_agent_runtime.types.return_control_payload

        out["returnControlPayload"] = (
            aws_sdk_bedrock_agent_runtime.types.return_control_payload.serialize_json(
                value["return_control_payload"]
            )
        )
    return out


def deserialize_json(data: dict) -> AgentCollaboratorOutputPayload:
    out: AgentCollaboratorOutputPayload = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_bedrock_agent_runtime.types.payload_type

        out["type"] = aws_sdk_bedrock_agent_runtime.types.payload_type.deserialize_json(
            data["type"]
        )
    if "text" in data:
        out["text"] = data["text"]
    if "returnControlPayload" in data:
        import aws_sdk_bedrock_agent_runtime.types.return_control_payload

        out["return_control_payload"] = (
            aws_sdk_bedrock_agent_runtime.types.return_control_payload.deserialize_json(
                data["returnControlPayload"]
            )
        )
    return out
