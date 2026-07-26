"""Generated from Smithy shape ``com.amazonaws.connect#AgentStatusSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.agent_status_summary

AgentStatusSummaryList: TypeAlias = list[
    "capo_connect.types.agent_status_summary.AgentStatusSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentStatusSummaryList) -> list:
    import capo_connect.types.agent_status_summary

    out: list = []
    for item in value:
        out.append(capo_connect.types.agent_status_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AgentStatusSummaryList:
    import capo_connect.types.agent_status_summary

    out: AgentStatusSummaryList = []
    for item in data:
        out.append(capo_connect.types.agent_status_summary.deserialize_json(item))
    return out
