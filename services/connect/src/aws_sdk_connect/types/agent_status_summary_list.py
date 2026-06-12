"""Generated from Smithy shape ``com.amazonaws.connect#AgentStatusSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.agent_status_summary

AgentStatusSummaryList: TypeAlias = list[
    "aws_sdk_connect.types.agent_status_summary.AgentStatusSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentStatusSummaryList) -> list:
    import aws_sdk_connect.types.agent_status_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.agent_status_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AgentStatusSummaryList:
    import aws_sdk_connect.types.agent_status_summary

    out: AgentStatusSummaryList = []
    for item in data:
        out.append(aws_sdk_connect.types.agent_status_summary.deserialize_json(item))
    return out
