"""Generated from Smithy shape ``com.amazonaws.macie2#SearchResourcesTagCriterion``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__list_of_search_resources_tag_criterion_pair
    import aws_sdk_macie2.types.search_resources_comparator


class SearchResourcesTagCriterion(TypedDict):
    comparator: NotRequired[
        "aws_sdk_macie2.types.search_resources_comparator.SearchResourcesComparator"
    ]
    """<p>The operator to use in the condition. Valid values are EQ (equals) and NE (not equals).</p>"""
    tag_values: NotRequired[
        "aws_sdk_macie2.types.__list_of_search_resources_tag_criterion_pair.__listOfSearchResourcesTagCriterionPair"
    ]
    """<p>The tag keys, tag values, or tag key and value pairs to use in the condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchResourcesTagCriterion) -> dict:
    out: dict = {}
    if "comparator" in value:
        import aws_sdk_macie2.types.search_resources_comparator

        out["comparator"] = (
            aws_sdk_macie2.types.search_resources_comparator.serialize_json(
                value["comparator"]
            )
        )
    if "tag_values" in value:
        import aws_sdk_macie2.types.__list_of_search_resources_tag_criterion_pair

        out["tagValues"] = (
            aws_sdk_macie2.types.__list_of_search_resources_tag_criterion_pair.serialize_json(
                value["tag_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> SearchResourcesTagCriterion:
    out: SearchResourcesTagCriterion = {}  # type: ignore[typeddict-item]
    if "comparator" in data:
        import aws_sdk_macie2.types.search_resources_comparator

        out["comparator"] = (
            aws_sdk_macie2.types.search_resources_comparator.deserialize_json(
                data["comparator"]
            )
        )
    if "tagValues" in data:
        import aws_sdk_macie2.types.__list_of_search_resources_tag_criterion_pair

        out["tag_values"] = (
            aws_sdk_macie2.types.__list_of_search_resources_tag_criterion_pair.deserialize_json(
                data["tagValues"]
            )
        )
    return out
