"""Generated from Smithy shape ``com.amazonaws.securityagent#AgentSpaceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.agent_space_summary

AgentSpaceSummaryList: TypeAlias = list[
    "capo_securityagent.types.agent_space_summary.AgentSpaceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentSpaceSummaryList) -> list:
    import capo_securityagent.types.agent_space_summary

    out: list = []
    for item in value:
        out.append(capo_securityagent.types.agent_space_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AgentSpaceSummaryList:
    import capo_securityagent.types.agent_space_summary

    out: AgentSpaceSummaryList = []
    for item in data:
        out.append(capo_securityagent.types.agent_space_summary.deserialize_json(item))
    return out
