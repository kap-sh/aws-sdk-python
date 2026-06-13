"""Generated from Smithy shape ``com.amazonaws.quicksight#AgentSearchFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.agent_search_filter

AgentSearchFilterList: TypeAlias = list[
    "aws_sdk_quicksight.types.agent_search_filter.AgentSearchFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentSearchFilterList) -> list:
    import aws_sdk_quicksight.types.agent_search_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.agent_search_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> AgentSearchFilterList:
    import aws_sdk_quicksight.types.agent_search_filter

    out: AgentSearchFilterList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.agent_search_filter.deserialize_json(item))
    return out
