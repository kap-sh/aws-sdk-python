"""Generated from Smithy shape ``com.amazonaws.connect#UserSearchConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.user_search_criteria

UserSearchConditionList: TypeAlias = list[
    "capo_connect.types.user_search_criteria.UserSearchCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: UserSearchConditionList) -> list:
    import capo_connect.types.user_search_criteria

    out: list = []
    for item in value:
        out.append(capo_connect.types.user_search_criteria.serialize_json(item))
    return out


def deserialize_json(data: list) -> UserSearchConditionList:
    import capo_connect.types.user_search_criteria

    out: UserSearchConditionList = []
    for item in data:
        out.append(capo_connect.types.user_search_criteria.deserialize_json(item))
    return out
