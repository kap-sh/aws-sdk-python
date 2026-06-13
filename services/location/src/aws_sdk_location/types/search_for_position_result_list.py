"""Generated from Smithy shape ``com.amazonaws.location#SearchForPositionResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_location.types.search_for_position_result

SearchForPositionResultList: TypeAlias = list[
    "aws_sdk_location.types.search_for_position_result.SearchForPositionResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchForPositionResultList) -> list:
    import aws_sdk_location.types.search_for_position_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_location.types.search_for_position_result.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SearchForPositionResultList:
    import aws_sdk_location.types.search_for_position_result

    out: SearchForPositionResultList = []
    for item in data:
        out.append(
            aws_sdk_location.types.search_for_position_result.deserialize_json(item)
        )
    return out
