"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AgentAliasSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.agent_alias_id
    import aws_sdk_bedrock_agent.types.agent_alias_routing_configuration
    import aws_sdk_bedrock_agent.types.agent_alias_status
    import aws_sdk_bedrock_agent.types.alias_invocation_state
    import aws_sdk_bedrock_agent.types.date_timestamp
    import aws_sdk_bedrock_agent.types.description
    import aws_sdk_bedrock_agent.types.name


class AgentAliasSummary(TypedDict):
    agent_alias_id: "aws_sdk_bedrock_agent.types.agent_alias_id.AgentAliasId"
    """<p>Contains details about </p>"""
    agent_alias_name: "aws_sdk_bedrock_agent.types.name.Name"
    """<p>The name of the alias.</p>"""
    description: NotRequired["aws_sdk_bedrock_agent.types.description.Description"]
    """<p>The description of the alias.</p>"""
    routing_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.agent_alias_routing_configuration.AgentAliasRoutingConfiguration"
    ]
    """<p>Contains details about the version of the agent with which the alias is associated.</p>"""
    agent_alias_status: (
        "aws_sdk_bedrock_agent.types.agent_alias_status.AgentAliasStatus"
    )
    """<p>The status of the alias.</p>"""
    created_at: "aws_sdk_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the alias of the agent was created.</p>"""
    updated_at: "aws_sdk_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the alias was last updated.</p>"""
    alias_invocation_state: NotRequired[
        "aws_sdk_bedrock_agent.types.alias_invocation_state.AliasInvocationState"
    ]
    """<p>The invocation state for the agent alias. If the agent alias is running, the value is <code>ACCEPT_INVOCATIONS</code>. If the agent alias is paused, the value is <code>REJECT_INVOCATIONS</code>. Use the <code>UpdateAgentAlias</code> operation to change the invocation state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentAliasSummary) -> dict:
    out: dict = {}
    out["agentAliasId"] = value["agent_alias_id"]
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
    import aws_sdk_bedrock_agent.types.agent_alias_status

    out["agentAliasStatus"] = (
        aws_sdk_bedrock_agent.types.agent_alias_status.serialize_json(
            value["agent_alias_status"]
        )
    )
    import aws_sdk_bedrock_agent.types.date_timestamp

    out["createdAt"] = aws_sdk_bedrock_agent.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_bedrock_agent.types.date_timestamp

    out["updatedAt"] = aws_sdk_bedrock_agent.types.date_timestamp.serialize_json(
        value["updated_at"]
    )
    if "alias_invocation_state" in value:
        import aws_sdk_bedrock_agent.types.alias_invocation_state

        out["aliasInvocationState"] = (
            aws_sdk_bedrock_agent.types.alias_invocation_state.serialize_json(
                value["alias_invocation_state"]
            )
        )
    return out


def deserialize_json(data: dict) -> AgentAliasSummary:
    out: AgentAliasSummary = {}  # type: ignore[typeddict-item]
    if "agentAliasId" in data:
        out["agent_alias_id"] = data["agentAliasId"]
    else:
        raise DeserializationError("AgentAliasSummary.agent_alias_id required")
    if "agentAliasName" in data:
        out["agent_alias_name"] = data["agentAliasName"]
    else:
        raise DeserializationError("AgentAliasSummary.agent_alias_name required")
    if "description" in data:
        out["description"] = data["description"]
    if "routingConfiguration" in data:
        import aws_sdk_bedrock_agent.types.agent_alias_routing_configuration

        out["routing_configuration"] = (
            aws_sdk_bedrock_agent.types.agent_alias_routing_configuration.deserialize_json(
                data["routingConfiguration"]
            )
        )
    if "agentAliasStatus" in data:
        import aws_sdk_bedrock_agent.types.agent_alias_status

        out["agent_alias_status"] = (
            aws_sdk_bedrock_agent.types.agent_alias_status.deserialize_json(
                data["agentAliasStatus"]
            )
        )
    else:
        raise DeserializationError("AgentAliasSummary.agent_alias_status required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agent.types.date_timestamp

        out["created_at"] = aws_sdk_bedrock_agent.types.date_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("AgentAliasSummary.created_at required")
    if "updatedAt" in data:
        import aws_sdk_bedrock_agent.types.date_timestamp

        out["updated_at"] = aws_sdk_bedrock_agent.types.date_timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("AgentAliasSummary.updated_at required")
    if "aliasInvocationState" in data:
        import aws_sdk_bedrock_agent.types.alias_invocation_state

        out["alias_invocation_state"] = (
            aws_sdk_bedrock_agent.types.alias_invocation_state.deserialize_json(
                data["aliasInvocationState"]
            )
        )
    return out
