"""Generated from Smithy shape ``com.amazonaws.macie2#SearchResourcesBucketCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.search_resources_criteria_block


class SearchResourcesBucketCriteria(TypedDict, closed=True):
    excludes: NotRequired[
        "aws_sdk_macie2.types.search_resources_criteria_block.SearchResourcesCriteriaBlock"
    ]
    """<p>The property- and tag-based conditions that determine which buckets to exclude from the results.</p>"""
    includes: NotRequired[
        "aws_sdk_macie2.types.search_resources_criteria_block.SearchResourcesCriteriaBlock"
    ]
    """<p>The property- and tag-based conditions that determine which buckets to include in the results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchResourcesBucketCriteria) -> dict:
    out: dict = {}
    if "excludes" in value:
        import aws_sdk_macie2.types.search_resources_criteria_block

        out["excludes"] = (
            aws_sdk_macie2.types.search_resources_criteria_block.serialize_json(
                value["excludes"]
            )
        )
    if "includes" in value:
        import aws_sdk_macie2.types.search_resources_criteria_block

        out["includes"] = (
            aws_sdk_macie2.types.search_resources_criteria_block.serialize_json(
                value["includes"]
            )
        )
    return out


def deserialize_json(data: dict) -> SearchResourcesBucketCriteria:
    out: SearchResourcesBucketCriteria = {}  # type: ignore[typeddict-item]
    if "excludes" in data:
        import aws_sdk_macie2.types.search_resources_criteria_block

        out["excludes"] = (
            aws_sdk_macie2.types.search_resources_criteria_block.deserialize_json(
                data["excludes"]
            )
        )
    if "includes" in data:
        import aws_sdk_macie2.types.search_resources_criteria_block

        out["includes"] = (
            aws_sdk_macie2.types.search_resources_criteria_block.deserialize_json(
                data["includes"]
            )
        )
    return out
