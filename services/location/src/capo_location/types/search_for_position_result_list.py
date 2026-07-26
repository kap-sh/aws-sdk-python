"""Generated from Smithy shape ``com.amazonaws.location#SearchForPositionResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_location.types.search_for_position_result

SearchForPositionResultList: TypeAlias = list[
    "capo_location.types.search_for_position_result.SearchForPositionResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchForPositionResultList) -> list:
    import capo_location.types.search_for_position_result

    out: list = []
    for item in value:
        out.append(capo_location.types.search_for_position_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> SearchForPositionResultList:
    import capo_location.types.search_for_position_result

    out: SearchForPositionResultList = []
    for item in data:
        out.append(
            capo_location.types.search_for_position_result.deserialize_json(item)
        )
    return out
