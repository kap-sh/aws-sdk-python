"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfSearchResourcesCriteria``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_macie2.types.search_resources_criteria

__listOfSearchResourcesCriteria: TypeAlias = list[
    "aws_sdk_macie2.types.search_resources_criteria.SearchResourcesCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfSearchResourcesCriteria) -> list:
    import aws_sdk_macie2.types.search_resources_criteria

    out: list = []
    for item in value:
        out.append(aws_sdk_macie2.types.search_resources_criteria.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfSearchResourcesCriteria:
    import aws_sdk_macie2.types.search_resources_criteria

    out: __listOfSearchResourcesCriteria = []
    for item in data:
        out.append(
            aws_sdk_macie2.types.search_resources_criteria.deserialize_json(item)
        )
    return out
