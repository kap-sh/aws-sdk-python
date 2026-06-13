"""Generated from Smithy shape ``com.amazonaws.quicksight#AgentSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.agent_summary

AgentSummaryList: TypeAlias = list[
    "aws_sdk_quicksight.types.agent_summary.AgentSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentSummaryList) -> list:
    import aws_sdk_quicksight.types.agent_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.agent_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AgentSummaryList:
    import aws_sdk_quicksight.types.agent_summary

    out: AgentSummaryList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.agent_summary.deserialize_json(item))
    return out
