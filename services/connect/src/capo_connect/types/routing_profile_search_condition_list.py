"""Generated from Smithy shape ``com.amazonaws.connect#RoutingProfileSearchConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.routing_profile_search_criteria

RoutingProfileSearchConditionList: TypeAlias = list[
    "capo_connect.types.routing_profile_search_criteria.RoutingProfileSearchCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: RoutingProfileSearchConditionList) -> list:
    import capo_connect.types.routing_profile_search_criteria

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.routing_profile_search_criteria.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RoutingProfileSearchConditionList:
    import capo_connect.types.routing_profile_search_criteria

    out: RoutingProfileSearchConditionList = []
    for item in data:
        out.append(
            capo_connect.types.routing_profile_search_criteria.deserialize_json(item)
        )
    return out
