"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AgentAliasHistoryEvents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.agent_alias_history_event

AgentAliasHistoryEvents: TypeAlias = list[
    "capo_bedrock_agent.types.agent_alias_history_event.AgentAliasHistoryEvent"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentAliasHistoryEvents) -> list:
    import capo_bedrock_agent.types.agent_alias_history_event

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent.types.agent_alias_history_event.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AgentAliasHistoryEvents:
    import capo_bedrock_agent.types.agent_alias_history_event

    out: AgentAliasHistoryEvents = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent.types.agent_alias_history_event.deserialize_json(item)
        )
    return out
