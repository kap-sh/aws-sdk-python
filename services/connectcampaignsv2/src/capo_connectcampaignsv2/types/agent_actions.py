"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#AgentActions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.agent_action

AgentActions: TypeAlias = list["capo_connectcampaignsv2.types.agent_action.AgentAction"]


# --- restJson1 ser/de ---
def serialize_json(value: AgentActions) -> list:
    return list(value)


def deserialize_json(data: list) -> AgentActions:
    return list(data)
