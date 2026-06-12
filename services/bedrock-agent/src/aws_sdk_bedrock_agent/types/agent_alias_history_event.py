"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AgentAliasHistoryEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.agent_alias_routing_configuration
    import aws_sdk_bedrock_agent.types.date_timestamp


class AgentAliasHistoryEvent(TypedDict):
    routing_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.agent_alias_routing_configuration.AgentAliasRoutingConfiguration"
    ]
    """<p>Contains details about the version of the agent with which the alias is associated.</p>"""
    end_date: NotRequired["aws_sdk_bedrock_agent.types.date_timestamp.DateTimestamp"]
    """<p>The date that the alias stopped being associated to the version in the <code>routingConfiguration</code> object</p>"""
    start_date: NotRequired["aws_sdk_bedrock_agent.types.date_timestamp.DateTimestamp"]
    """<p>The date that the alias began being associated to the version in the <code>routingConfiguration</code> object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentAliasHistoryEvent) -> dict:
    out: dict = {}
    if "routing_configuration" in value:
        import aws_sdk_bedrock_agent.types.agent_alias_routing_configuration

        out["routingConfiguration"] = (
            aws_sdk_bedrock_agent.types.agent_alias_routing_configuration.serialize_json(
                value["routing_configuration"]
            )
        )
    if "end_date" in value:
        import aws_sdk_bedrock_agent.types.date_timestamp

        out["endDate"] = aws_sdk_bedrock_agent.types.date_timestamp.serialize_json(
            value["end_date"]
        )
    if "start_date" in value:
        import aws_sdk_bedrock_agent.types.date_timestamp

        out["startDate"] = aws_sdk_bedrock_agent.types.date_timestamp.serialize_json(
            value["start_date"]
        )
    return out


def deserialize_json(data: dict) -> AgentAliasHistoryEvent:
    out: AgentAliasHistoryEvent = {}  # type: ignore[typeddict-item]
    if "routingConfiguration" in data:
        import aws_sdk_bedrock_agent.types.agent_alias_routing_configuration

        out["routing_configuration"] = (
            aws_sdk_bedrock_agent.types.agent_alias_routing_configuration.deserialize_json(
                data["routingConfiguration"]
            )
        )
    if "endDate" in data:
        import aws_sdk_bedrock_agent.types.date_timestamp

        out["end_date"] = aws_sdk_bedrock_agent.types.date_timestamp.deserialize_json(
            data["endDate"]
        )
    if "startDate" in data:
        import aws_sdk_bedrock_agent.types.date_timestamp

        out["start_date"] = aws_sdk_bedrock_agent.types.date_timestamp.deserialize_json(
            data["startDate"]
        )
    return out
