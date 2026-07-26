"""Generated from Smithy shape ``com.amazonaws.quicksight#AgentSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.agent_summary

AgentSummaries: TypeAlias = list["capo_quicksight.types.agent_summary.AgentSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: AgentSummaries) -> list:
    import capo_quicksight.types.agent_summary

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.agent_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AgentSummaries:
    import capo_quicksight.types.agent_summary

    out: AgentSummaries = []
    for item in data:
        out.append(capo_quicksight.types.agent_summary.deserialize_json(item))
    return out
