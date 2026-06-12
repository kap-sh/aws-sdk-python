"""Generated from Smithy shape ``com.amazonaws.macie2#SearchResourcesCriteria``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.search_resources_simple_criterion
    import aws_sdk_macie2.types.search_resources_tag_criterion


class SearchResourcesCriteria(TypedDict):
    simple_criterion: NotRequired[
        "aws_sdk_macie2.types.search_resources_simple_criterion.SearchResourcesSimpleCriterion"
    ]
    """<p>A property-based condition that defines a property, operator, and one or more values for including or excluding resources from the results.</p>"""
    tag_criterion: NotRequired[
        "aws_sdk_macie2.types.search_resources_tag_criterion.SearchResourcesTagCriterion"
    ]
    """<p>A tag-based condition that defines an operator and tag keys, tag values, or tag key and value pairs for including or excluding resources from the results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchResourcesCriteria) -> dict:
    out: dict = {}
    if "simple_criterion" in value:
        import aws_sdk_macie2.types.search_resources_simple_criterion

        out["simpleCriterion"] = (
            aws_sdk_macie2.types.search_resources_simple_criterion.serialize_json(
                value["simple_criterion"]
            )
        )
    if "tag_criterion" in value:
        import aws_sdk_macie2.types.search_resources_tag_criterion

        out["tagCriterion"] = (
            aws_sdk_macie2.types.search_resources_tag_criterion.serialize_json(
                value["tag_criterion"]
            )
        )
    return out


def deserialize_json(data: dict) -> SearchResourcesCriteria:
    out: SearchResourcesCriteria = {}  # type: ignore[typeddict-item]
    if "simpleCriterion" in data:
        import aws_sdk_macie2.types.search_resources_simple_criterion

        out["simple_criterion"] = (
            aws_sdk_macie2.types.search_resources_simple_criterion.deserialize_json(
                data["simpleCriterion"]
            )
        )
    if "tagCriterion" in data:
        import aws_sdk_macie2.types.search_resources_tag_criterion

        out["tag_criterion"] = (
            aws_sdk_macie2.types.search_resources_tag_criterion.deserialize_json(
                data["tagCriterion"]
            )
        )
    return out
