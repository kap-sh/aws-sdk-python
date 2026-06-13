"""Generated from Smithy shape ``com.amazonaws.quicksight#SearchFlowsFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.search_flows_filter

SearchFlowsFilterList: TypeAlias = list[
    "aws_sdk_quicksight.types.search_flows_filter.SearchFlowsFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchFlowsFilterList) -> list:
    import aws_sdk_quicksight.types.search_flows_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.search_flows_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> SearchFlowsFilterList:
    import aws_sdk_quicksight.types.search_flows_filter

    out: SearchFlowsFilterList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.search_flows_filter.deserialize_json(item))
    return out
