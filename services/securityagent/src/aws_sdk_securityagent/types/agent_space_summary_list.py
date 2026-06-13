"""Generated from Smithy shape ``com.amazonaws.securityagent#AgentSpaceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.agent_space_summary

AgentSpaceSummaryList: TypeAlias = list[
    "aws_sdk_securityagent.types.agent_space_summary.AgentSpaceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentSpaceSummaryList) -> list:
    import aws_sdk_securityagent.types.agent_space_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_securityagent.types.agent_space_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AgentSpaceSummaryList:
    import aws_sdk_securityagent.types.agent_space_summary

    out: AgentSpaceSummaryList = []
    for item in data:
        out.append(
            aws_sdk_securityagent.types.agent_space_summary.deserialize_json(item)
        )
    return out
