"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfSearchResourcesTagCriterionPair``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_macie2.types.search_resources_tag_criterion_pair

__listOfSearchResourcesTagCriterionPair: TypeAlias = list[
    "capo_macie2.types.search_resources_tag_criterion_pair.SearchResourcesTagCriterionPair"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfSearchResourcesTagCriterionPair) -> list:
    import capo_macie2.types.search_resources_tag_criterion_pair

    out: list = []
    for item in value:
        out.append(
            capo_macie2.types.search_resources_tag_criterion_pair.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfSearchResourcesTagCriterionPair:
    import capo_macie2.types.search_resources_tag_criterion_pair

    out: __listOfSearchResourcesTagCriterionPair = []
    for item in data:
        out.append(
            capo_macie2.types.search_resources_tag_criterion_pair.deserialize_json(item)
        )
    return out
