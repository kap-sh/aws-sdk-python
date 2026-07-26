"""Generated from Smithy shape ``com.amazonaws.connect#UserHierarchyGroupSearchConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.user_hierarchy_group_search_criteria

UserHierarchyGroupSearchConditionList: TypeAlias = list[
    "capo_connect.types.user_hierarchy_group_search_criteria.UserHierarchyGroupSearchCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: UserHierarchyGroupSearchConditionList) -> list:
    import capo_connect.types.user_hierarchy_group_search_criteria

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.user_hierarchy_group_search_criteria.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> UserHierarchyGroupSearchConditionList:
    import capo_connect.types.user_hierarchy_group_search_criteria

    out: UserHierarchyGroupSearchConditionList = []
    for item in data:
        out.append(
            capo_connect.types.user_hierarchy_group_search_criteria.deserialize_json(
                item
            )
        )
    return out
