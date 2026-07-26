"""Generated from Smithy shape ``com.amazonaws.connect#ViewSearchConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.view_search_criteria

ViewSearchConditionList: TypeAlias = list[
    "capo_connect.types.view_search_criteria.ViewSearchCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: ViewSearchConditionList) -> list:
    import capo_connect.types.view_search_criteria

    out: list = []
    for item in value:
        out.append(capo_connect.types.view_search_criteria.serialize_json(item))
    return out


def deserialize_json(data: list) -> ViewSearchConditionList:
    import capo_connect.types.view_search_criteria

    out: ViewSearchConditionList = []
    for item in data:
        out.append(capo_connect.types.view_search_criteria.deserialize_json(item))
    return out
