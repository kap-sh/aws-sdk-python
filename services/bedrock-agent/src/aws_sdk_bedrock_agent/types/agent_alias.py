"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AgentAlias``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.agent_alias_arn
    import aws_sdk_bedrock_agent.types.agent_alias_history_events
    import aws_sdk_bedrock_agent.types.agent_alias_id
    import aws_sdk_bedrock_agent.types.agent_alias_routing_configuration
    import aws_sdk_bedrock_agent.types.agent_alias_status
    import aws_sdk_bedrock_agent.types.alias_invocation_state
    import aws_sdk_bedrock_agent.types.client_token
    import aws_sdk_bedrock_agent.types.date_timestamp
    import aws_sdk_bedrock_agent.types.description
    import aws_sdk_bedrock_agent.types.failure_reasons
    import aws_sdk_bedrock_agent.types.id
    import aws_sdk_bedrock_agent.types.name


class AgentAlias(TypedDict):
    agent_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the agent.</p>"""
    agent_alias_id: "aws_sdk_bedrock_agent.types.agent_alias_id.AgentAliasId"
    """<p>The unique identifier of the alias of the agent.</p>"""
    agent_alias_name: "aws_sdk_bedrock_agent.types.name.Name"
    """<p>The name of the alias of the agent.</p>"""
    agent_alias_arn: "aws_sdk_bedrock_agent.types.agent_alias_arn.AgentAliasArn"
    """<p>The Amazon Resource Name (ARN) of the alias of the agent.</p>"""
    client_token: NotRequired["aws_sdk_bedrock_agent.types.client_token.ClientToken"]
    r"""<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>"""
    description: NotRequired["aws_sdk_bedrock_agent.types.description.Description"]
    """<p>The description of the alias of the agent.</p>"""
    routing_configuration: "aws_sdk_bedrock_agent.types.agent_alias_routing_configuration.AgentAliasRoutingConfiguration"
    """<p>Contains details about the routing configuration of the alias.</p>"""
    created_at: "aws_sdk_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the alias of the agent was created.</p>"""
    updated_at: "aws_sdk_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the alias was last updated.</p>"""
    agent_alias_history_events: NotRequired[
        "aws_sdk_bedrock_agent.types.agent_alias_history_events.AgentAliasHistoryEvents"
    ]
    """<p>Contains details about the history of the alias.</p>"""
    agent_alias_status: (
        "aws_sdk_bedrock_agent.types.agent_alias_status.AgentAliasStatus"
    )
    """<p>The status of the alias of the agent and whether it is ready for use. The following statuses are possible:</p> <ul> <li> <p>CREATING – The agent alias is being created.</p> </li> <li> <p>PREPARED – The agent alias is finished being created or updated and is ready to be invoked.</p> </li> <li> <p>FAILED – The agent alias API operation failed.</p> </li> <li> <p>UPDATING – The agent alias is being updated.</p> </li> <li> <p>DELETING – The agent alias is being deleted.</p> </li> <li> <p>DISSOCIATED - The agent alias has no version associated with it.</p> </li> </ul>"""
    failure_reasons: NotRequired[
        "aws_sdk_bedrock_agent.types.failure_reasons.FailureReasons"
    ]
    """<p>Information on the failure of Provisioned Throughput assigned to an agent alias.</p>"""
    alias_invocation_state: NotRequired[
        "aws_sdk_bedrock_agent.types.alias_invocation_state.AliasInvocationState"
    ]
    """<p>The invocation state for the agent alias. If the agent alias is running, the value is <code>ACCEPT_INVOCATIONS</code>. If the agent alias is paused, the value is <code>REJECT_INVOCATIONS</code>. Use the <code>UpdateAgentAlias</code> operation to change the invocation state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentAlias) -> dict:
    out: dict = {}
    out["agentId"] = value["agent_id"]
    out["agentAliasId"] = value["agent_alias_id"]
    out["agentAliasName"] = value["agent_alias_name"]
    out["agentAliasArn"] = value["agent_alias_arn"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_bedrock_agent.types.agent_alias_routing_configuration

    out["routingConfiguration"] = (
        aws_sdk_bedrock_agent.types.agent_alias_routing_configuration.serialize_json(
            value["routing_configuration"]
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
    if "agent_alias_history_events" in value:
        import aws_sdk_bedrock_agent.types.agent_alias_history_events

        out["agentAliasHistoryEvents"] = (
            aws_sdk_bedrock_agent.types.agent_alias_history_events.serialize_json(
                value["agent_alias_history_events"]
            )
        )
    import aws_sdk_bedrock_agent.types.agent_alias_status

    out["agentAliasStatus"] = (
        aws_sdk_bedrock_agent.types.agent_alias_status.serialize_json(
            value["agent_alias_status"]
        )
    )
    if "failure_reasons" in value:
        import aws_sdk_bedrock_agent.types.failure_reasons

        out["failureReasons"] = (
            aws_sdk_bedrock_agent.types.failure_reasons.serialize_json(
                value["failure_reasons"]
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


def deserialize_json(data: dict) -> AgentAlias:
    out: AgentAlias = {}  # type: ignore[typeddict-item]
    if "agentId" in data:
        out["agent_id"] = data["agentId"]
    else:
        raise DeserializationError("AgentAlias.agent_id required")
    if "agentAliasId" in data:
        out["agent_alias_id"] = data["agentAliasId"]
    else:
        raise DeserializationError("AgentAlias.agent_alias_id required")
    if "agentAliasName" in data:
        out["agent_alias_name"] = data["agentAliasName"]
    else:
        raise DeserializationError("AgentAlias.agent_alias_name required")
    if "agentAliasArn" in data:
        out["agent_alias_arn"] = data["agentAliasArn"]
    else:
        raise DeserializationError("AgentAlias.agent_alias_arn required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "description" in data:
        out["description"] = data["description"]
    if "routingConfiguration" in data:
        import aws_sdk_bedrock_agent.types.agent_alias_routing_configuration

        out["routing_configuration"] = (
            aws_sdk_bedrock_agent.types.agent_alias_routing_configuration.deserialize_json(
                data["routingConfiguration"]
            )
        )
    else:
        raise DeserializationError("AgentAlias.routing_configuration required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agent.types.date_timestamp

        out["created_at"] = aws_sdk_bedrock_agent.types.date_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("AgentAlias.created_at required")
    if "updatedAt" in data:
        import aws_sdk_bedrock_agent.types.date_timestamp

        out["updated_at"] = aws_sdk_bedrock_agent.types.date_timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("AgentAlias.updated_at required")
    if "agentAliasHistoryEvents" in data:
        import aws_sdk_bedrock_agent.types.agent_alias_history_events

        out["agent_alias_history_events"] = (
            aws_sdk_bedrock_agent.types.agent_alias_history_events.deserialize_json(
                data["agentAliasHistoryEvents"]
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
        raise DeserializationError("AgentAlias.agent_alias_status required")
    if "failureReasons" in data:
        import aws_sdk_bedrock_agent.types.failure_reasons

        out["failure_reasons"] = (
            aws_sdk_bedrock_agent.types.failure_reasons.deserialize_json(
                data["failureReasons"]
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
