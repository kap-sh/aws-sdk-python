"""Generated from Smithy shape ``com.amazonaws.bedrockagent#UpdateAgentAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.agent_alias_id
    import aws_sdk_bedrock_agent.types.agent_alias_routing_configuration
    import aws_sdk_bedrock_agent.types.alias_invocation_state
    import aws_sdk_bedrock_agent.types.description
    import aws_sdk_bedrock_agent.types.id
    import aws_sdk_bedrock_agent.types.name


class UpdateAgentAliasRequest(TypedDict, closed=True):
    agent_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the agent.</p>"""
    agent_alias_id: "aws_sdk_bedrock_agent.types.agent_alias_id.AgentAliasId"
    """<p>The unique identifier of the alias.</p>"""
    agent_alias_name: "aws_sdk_bedrock_agent.types.name.Name"
    """<p>Specifies a new name for the alias.</p>"""
    description: NotRequired["aws_sdk_bedrock_agent.types.description.Description"]
    """<p>Specifies a new description for the alias.</p>"""
    routing_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.agent_alias_routing_configuration.AgentAliasRoutingConfiguration"
    ]
    """<p>Contains details about the routing configuration of the alias.</p>"""
    alias_invocation_state: NotRequired[
        "aws_sdk_bedrock_agent.types.alias_invocation_state.AliasInvocationState"
    ]
    """<p>The invocation state for the agent alias. To pause the agent alias, set the value to <code>REJECT_INVOCATIONS</code>. To start the agent alias running again, set the value to <code>ACCEPT_INVOCATIONS</code>. Use the <code>GetAgentAlias</code>, or <code>ListAgentAliases</code>, operation to get the invocation state of an agent alias.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentAliasRequest) -> dict:
    out: dict = {}
    out["agentAliasName"] = value["agent_alias_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "routing_configuration" in value:
        import aws_sdk_bedrock_agent.types.agent_alias_routing_configuration

        out["routingConfiguration"] = (
            aws_sdk_bedrock_agent.types.agent_alias_routing_configuration.serialize_json(
                value["routing_configuration"]
            )
        )
    if "alias_invocation_state" in value:
        import aws_sdk_bedrock_agent.types.alias_invocation_state

        out["aliasInvocationState"] = (
            aws_sdk_bedrock_agent.types.alias_invocation_state.serialize_json(
                value["alias_invocation_state"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAgentAliasRequest:
    out: UpdateAgentAliasRequest = {}  # type: ignore[typeddict-item]
    if "agentAliasName" in data:
        out["agent_alias_name"] = data["agentAliasName"]
    else:
        raise DeserializationError("UpdateAgentAliasRequest.agent_alias_name required")
    if "description" in data:
        out["description"] = data["description"]
    if "routingConfiguration" in data:
        import aws_sdk_bedrock_agent.types.agent_alias_routing_configuration

        out["routing_configuration"] = (
            aws_sdk_bedrock_agent.types.agent_alias_routing_configuration.deserialize_json(
                data["routingConfiguration"]
            )
        )
    if "aliasInvocationState" in data:
        import aws_sdk_bedrock_agent.types.alias_invocation_state

        out["alias_invocation_state"] = (
            aws_sdk_bedrock_agent.types.alias_invocation_state.deserialize_json(
                data["aliasInvocationState"]
            )
        )
    return out
