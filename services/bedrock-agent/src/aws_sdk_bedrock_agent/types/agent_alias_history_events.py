"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AgentAliasHistoryEvents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.agent_alias_history_event

AgentAliasHistoryEvents: TypeAlias = list[
    "aws_sdk_bedrock_agent.types.agent_alias_history_event.AgentAliasHistoryEvent"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentAliasHistoryEvents) -> list:
    import aws_sdk_bedrock_agent.types.agent_alias_history_event

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agent.types.agent_alias_history_event.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AgentAliasHistoryEvents:
    import aws_sdk_bedrock_agent.types.agent_alias_history_event

    out: AgentAliasHistoryEvents = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent.types.agent_alias_history_event.deserialize_json(item)
        )
    return out
