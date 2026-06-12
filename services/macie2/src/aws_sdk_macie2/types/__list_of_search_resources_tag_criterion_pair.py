"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfSearchResourcesTagCriterionPair``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_macie2.types.search_resources_tag_criterion_pair

__listOfSearchResourcesTagCriterionPair: TypeAlias = list[
    "aws_sdk_macie2.types.search_resources_tag_criterion_pair.SearchResourcesTagCriterionPair"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfSearchResourcesTagCriterionPair) -> list:
    import aws_sdk_macie2.types.search_resources_tag_criterion_pair

    out: list = []
    for item in value:
        out.append(
            aws_sdk_macie2.types.search_resources_tag_criterion_pair.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfSearchResourcesTagCriterionPair:
    import aws_sdk_macie2.types.search_resources_tag_criterion_pair

    out: __listOfSearchResourcesTagCriterionPair = []
    for item in data:
        out.append(
            aws_sdk_macie2.types.search_resources_tag_criterion_pair.deserialize_json(
                item
            )
        )
    return out
