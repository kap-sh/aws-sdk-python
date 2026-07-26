"""Generated from Smithy shape ``com.amazonaws.connect#QuickConnectSearchConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.quick_connect_search_criteria

QuickConnectSearchConditionList: TypeAlias = list[
    "capo_connect.types.quick_connect_search_criteria.QuickConnectSearchCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: QuickConnectSearchConditionList) -> list:
    import capo_connect.types.quick_connect_search_criteria

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.quick_connect_search_criteria.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> QuickConnectSearchConditionList:
    import capo_connect.types.quick_connect_search_criteria

    out: QuickConnectSearchConditionList = []
    for item in data:
        out.append(
            capo_connect.types.quick_connect_search_criteria.deserialize_json(item)
        )
    return out
