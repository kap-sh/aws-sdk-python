"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgentCollaboratorInputPayload``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.agent_collaborator_payload_string
    import aws_sdk_bedrock_agent_runtime.types.payload_type
    import aws_sdk_bedrock_agent_runtime.types.return_control_results


class AgentCollaboratorInputPayload(TypedDict):
    type: NotRequired["aws_sdk_bedrock_agent_runtime.types.payload_type.PayloadType"]
    """<p>The input type.</p>"""
    text: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.agent_collaborator_payload_string.AgentCollaboratorPayloadString"
    ]
    """<p>Input text.</p>"""
    return_control_results: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.return_control_results.ReturnControlResults"
    ]
    """<p>An action invocation result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentCollaboratorInputPayload) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_bedrock_agent_runtime.types.payload_type

        out["type"] = aws_sdk_bedrock_agent_runtime.types.payload_type.serialize_json(
            value["type"]
        )
    if "text" in value:
        out["text"] = value["text"]
    if "return_control_results" in value:
        import aws_sdk_bedrock_agent_runtime.types.return_control_results

        out["returnControlResults"] = (
            aws_sdk_bedrock_agent_runtime.types.return_control_results.serialize_json(
                value["return_control_results"]
            )
        )
    return out


def deserialize_json(data: dict) -> AgentCollaboratorInputPayload:
    out: AgentCollaboratorInputPayload = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_bedrock_agent_runtime.types.payload_type

        out["type"] = aws_sdk_bedrock_agent_runtime.types.payload_type.deserialize_json(
            data["type"]
        )
    if "text" in data:
        out["text"] = data["text"]
    if "returnControlResults" in data:
        import aws_sdk_bedrock_agent_runtime.types.return_control_results

        out["return_control_results"] = (
            aws_sdk_bedrock_agent_runtime.types.return_control_results.deserialize_json(
                data["returnControlResults"]
            )
        )
    return out
