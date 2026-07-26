"""Generated from Smithy shape ``com.amazonaws.glue#ListDataQualityRulesetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.data_quality_ruleset_filter_criteria
    import capo_glue.types.page_size
    import capo_glue.types.pagination_token
    import capo_glue.types.tags_map


class ListDataQualityRulesetsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_glue.types.pagination_token.PaginationToken"]
    """<p>A paginated token to offset the results.</p>"""
    max_results: NotRequired["capo_glue.types.page_size.PageSize"]
    """<p>The maximum number of results to return.</p>"""
    filter: NotRequired[
        "capo_glue.types.data_quality_ruleset_filter_criteria.DataQualityRulesetFilterCriteria"
    ]
    """<p>The filter criteria. </p>"""
    tags: NotRequired["capo_glue.types.tags_map.TagsMap"]
    """<p>A list of key-value pair tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDataQualityRulesetsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "filter" in value:
        import capo_glue.types.data_quality_ruleset_filter_criteria

        out["Filter"] = (
            capo_glue.types.data_quality_ruleset_filter_criteria.serialize_aws_json_1_1(
                value["filter"]
            )
        )
    if "tags" in value:
        import capo_glue.types.tags_map

        out["Tags"] = capo_glue.types.tags_map.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDataQualityRulesetsRequest:
    out: ListDataQualityRulesetsRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "Filter" in data:
        import capo_glue.types.data_quality_ruleset_filter_criteria

        out["filter"] = (
            capo_glue.types.data_quality_ruleset_filter_criteria.deserialize_aws_json_1_1(
                data["Filter"]
            )
        )
    if "Tags" in data:
        import capo_glue.types.tags_map

        out["tags"] = capo_glue.types.tags_map.deserialize_aws_json_1_1(data["Tags"])
    return out
