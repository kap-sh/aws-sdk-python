"""Generated from Smithy shape ``com.amazonaws.location#SearchForSuggestionsResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_location.types.search_for_suggestions_result

SearchForSuggestionsResultList: TypeAlias = list[
    "aws_sdk_location.types.search_for_suggestions_result.SearchForSuggestionsResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchForSuggestionsResultList) -> list:
    import aws_sdk_location.types.search_for_suggestions_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_location.types.search_for_suggestions_result.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SearchForSuggestionsResultList:
    import aws_sdk_location.types.search_for_suggestions_result

    out: SearchForSuggestionsResultList = []
    for item in data:
        out.append(
            aws_sdk_location.types.search_for_suggestions_result.deserialize_json(item)
        )
    return out
