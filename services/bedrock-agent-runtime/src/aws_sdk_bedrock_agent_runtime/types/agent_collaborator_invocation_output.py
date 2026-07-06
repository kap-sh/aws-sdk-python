"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgentCollaboratorInvocationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.agent_alias_arn
    import aws_sdk_bedrock_agent_runtime.types.agent_collaborator_output_payload
    import aws_sdk_bedrock_agent_runtime.types.metadata


class AgentCollaboratorInvocationOutput(TypedDict, closed=True):
    agent_collaborator_name: NotRequired["str"]
    """<p>The output's agent collaborator name.</p>"""
    agent_collaborator_alias_arn: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.agent_alias_arn.AgentAliasArn"
    ]
    """<p>The output's agent collaborator alias ARN.</p>"""
    output: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.agent_collaborator_output_payload.AgentCollaboratorOutputPayload"
    ]
    """<p>The output's output.</p>"""
    metadata: NotRequired["aws_sdk_bedrock_agent_runtime.types.metadata.Metadata"]
    """<p>Contains information about the output from the agent collaborator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentCollaboratorInvocationOutput) -> dict:
    out: dict = {}
    if "agent_collaborator_name" in value:
        out["agentCollaboratorName"] = value["agent_collaborator_name"]
    if "agent_collaborator_alias_arn" in value:
        out["agentCollaboratorAliasArn"] = value["agent_collaborator_alias_arn"]
    if "output" in value:
        import aws_sdk_bedrock_agent_runtime.types.agent_collaborator_output_payload

        out["output"] = (
            aws_sdk_bedrock_agent_runtime.types.agent_collaborator_output_payload.serialize_json(
                value["output"]
            )
        )
    if "metadata" in value:
        import aws_sdk_bedrock_agent_runtime.types.metadata

        out["metadata"] = aws_sdk_bedrock_agent_runtime.types.metadata.serialize_json(
            value["metadata"]
        )
    return out


def deserialize_json(data: dict) -> AgentCollaboratorInvocationOutput:
    out: AgentCollaboratorInvocationOutput = {}  # type: ignore[typeddict-item]
    if "agentCollaboratorName" in data:
        out["agent_collaborator_name"] = data["agentCollaboratorName"]
    if "agentCollaboratorAliasArn" in data:
        out["agent_collaborator_alias_arn"] = data["agentCollaboratorAliasArn"]
    if "output" in data:
        import aws_sdk_bedrock_agent_runtime.types.agent_collaborator_output_payload

        out["output"] = (
            aws_sdk_bedrock_agent_runtime.types.agent_collaborator_output_payload.deserialize_json(
                data["output"]
            )
        )
    if "metadata" in data:
        import aws_sdk_bedrock_agent_runtime.types.metadata

        out["metadata"] = aws_sdk_bedrock_agent_runtime.types.metadata.deserialize_json(
            data["metadata"]
        )
    return out
