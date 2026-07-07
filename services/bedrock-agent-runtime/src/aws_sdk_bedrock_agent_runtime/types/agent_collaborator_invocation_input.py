"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgentCollaboratorInvocationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.agent_alias_arn
    import aws_sdk_bedrock_agent_runtime.types.agent_collaborator_input_payload


class AgentCollaboratorInvocationInput(TypedDict, closed=True):
    agent_collaborator_name: NotRequired["str"]
    """<p>The collaborator's name.</p>"""
    agent_collaborator_alias_arn: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.agent_alias_arn.AgentAliasArn"
    ]
    """<p>The collaborator's alias ARN.</p>"""
    input: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.agent_collaborator_input_payload.AgentCollaboratorInputPayload"
    ]
    """<p>Text or action invocation result input for the collaborator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentCollaboratorInvocationInput) -> dict:
    out: dict = {}
    if "agent_collaborator_name" in value:
        out["agentCollaboratorName"] = value["agent_collaborator_name"]
    if "agent_collaborator_alias_arn" in value:
        out["agentCollaboratorAliasArn"] = value["agent_collaborator_alias_arn"]
    if "input" in value:
        import aws_sdk_bedrock_agent_runtime.types.agent_collaborator_input_payload

        out["input"] = (
            aws_sdk_bedrock_agent_runtime.types.agent_collaborator_input_payload.serialize_json(
                value["input"]
            )
        )
    return out


def deserialize_json(data: dict) -> AgentCollaboratorInvocationInput:
    out: AgentCollaboratorInvocationInput = {}  # type: ignore[typeddict-item]
    if "agentCollaboratorName" in data:
        out["agent_collaborator_name"] = data["agentCollaboratorName"]
    if "agentCollaboratorAliasArn" in data:
        out["agent_collaborator_alias_arn"] = data["agentCollaboratorAliasArn"]
    if "input" in data:
        import aws_sdk_bedrock_agent_runtime.types.agent_collaborator_input_payload

        out["input"] = (
            aws_sdk_bedrock_agent_runtime.types.agent_collaborator_input_payload.deserialize_json(
                data["input"]
            )
        )
    return out
