"""Generated from Smithy shape ``com.amazonaws.glue#ListDataQualityRulesetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.data_quality_ruleset_filter_criteria
    import aws_sdk_glue.types.page_size
    import aws_sdk_glue.types.pagination_token
    import aws_sdk_glue.types.tags_map


class ListDataQualityRulesetsRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_glue.types.pagination_token.PaginationToken"]
    """<p>A paginated token to offset the results.</p>"""
    max_results: NotRequired["aws_sdk_glue.types.page_size.PageSize"]
    """<p>The maximum number of results to return.</p>"""
    filter: NotRequired[
        "aws_sdk_glue.types.data_quality_ruleset_filter_criteria.DataQualityRulesetFilterCriteria"
    ]
    """<p>The filter criteria. </p>"""
    tags: NotRequired["aws_sdk_glue.types.tags_map.TagsMap"]
    """<p>A list of key-value pair tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDataQualityRulesetsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "filter" in value:
        import aws_sdk_glue.types.data_quality_ruleset_filter_criteria

        out["Filter"] = (
            aws_sdk_glue.types.data_quality_ruleset_filter_criteria.serialize_aws_json_1_1(
                value["filter"]
            )
        )
    if "tags" in value:
        import aws_sdk_glue.types.tags_map

        out["Tags"] = aws_sdk_glue.types.tags_map.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDataQualityRulesetsRequest:
    out: ListDataQualityRulesetsRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "Filter" in data:
        import aws_sdk_glue.types.data_quality_ruleset_filter_criteria

        out["filter"] = (
            aws_sdk_glue.types.data_quality_ruleset_filter_criteria.deserialize_aws_json_1_1(
                data["Filter"]
            )
        )
    if "Tags" in data:
        import aws_sdk_glue.types.tags_map

        out["tags"] = aws_sdk_glue.types.tags_map.deserialize_aws_json_1_1(data["Tags"])
    return out
