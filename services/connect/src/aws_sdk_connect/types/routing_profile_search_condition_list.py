"""Generated from Smithy shape ``com.amazonaws.connect#RoutingProfileSearchConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.routing_profile_search_criteria

RoutingProfileSearchConditionList: TypeAlias = list[
    "aws_sdk_connect.types.routing_profile_search_criteria.RoutingProfileSearchCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: RoutingProfileSearchConditionList) -> list:
    import aws_sdk_connect.types.routing_profile_search_criteria

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.routing_profile_search_criteria.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RoutingProfileSearchConditionList:
    import aws_sdk_connect.types.routing_profile_search_criteria

    out: RoutingProfileSearchConditionList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.routing_profile_search_criteria.deserialize_json(item)
        )
    return out
