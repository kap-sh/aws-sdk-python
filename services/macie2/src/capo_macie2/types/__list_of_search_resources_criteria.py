"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfSearchResourcesCriteria``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_macie2.types.search_resources_criteria

__listOfSearchResourcesCriteria: TypeAlias = list[
    "capo_macie2.types.search_resources_criteria.SearchResourcesCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfSearchResourcesCriteria) -> list:
    import capo_macie2.types.search_resources_criteria

    out: list = []
    for item in value:
        out.append(capo_macie2.types.search_resources_criteria.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfSearchResourcesCriteria:
    import capo_macie2.types.search_resources_criteria

    out: __listOfSearchResourcesCriteria = []
    for item in data:
        out.append(capo_macie2.types.search_resources_criteria.deserialize_json(item))
    return out
