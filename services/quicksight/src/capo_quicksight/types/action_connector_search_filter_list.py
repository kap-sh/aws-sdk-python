"""Generated from Smithy shape ``com.amazonaws.quicksight#ActionConnectorSearchFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.action_connector_search_filter

ActionConnectorSearchFilterList: TypeAlias = list[
    "capo_quicksight.types.action_connector_search_filter.ActionConnectorSearchFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ActionConnectorSearchFilterList) -> list:
    import capo_quicksight.types.action_connector_search_filter

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.action_connector_search_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ActionConnectorSearchFilterList:
    import capo_quicksight.types.action_connector_search_filter

    out: ActionConnectorSearchFilterList = []
    for item in data:
        out.append(
            capo_quicksight.types.action_connector_search_filter.deserialize_json(item)
        )
    return out
