"""Generated from Smithy shape ``com.amazonaws.location#SearchForTextResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_location.types.search_for_text_result

SearchForTextResultList: TypeAlias = list[
    "aws_sdk_location.types.search_for_text_result.SearchForTextResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchForTextResultList) -> list:
    import aws_sdk_location.types.search_for_text_result

    out: list = []
    for item in value:
        out.append(aws_sdk_location.types.search_for_text_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> SearchForTextResultList:
    import aws_sdk_location.types.search_for_text_result

    out: SearchForTextResultList = []
    for item in data:
        out.append(aws_sdk_location.types.search_for_text_result.deserialize_json(item))
    return out
