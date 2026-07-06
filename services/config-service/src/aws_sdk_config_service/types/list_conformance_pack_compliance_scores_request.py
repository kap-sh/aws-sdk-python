"""Generated from Smithy shape ``com.amazonaws.configservice#ListConformancePackComplianceScoresRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.conformance_pack_compliance_scores_filters
    import aws_sdk_config_service.types.next_token
    import aws_sdk_config_service.types.page_size_limit
    import aws_sdk_config_service.types.sort_by
    import aws_sdk_config_service.types.sort_order


class ListConformancePackComplianceScoresRequest(TypedDict, closed=True):
    filters: NotRequired[
        "aws_sdk_config_service.types.conformance_pack_compliance_scores_filters.ConformancePackComplianceScoresFilters"
    ]
    """<p>Filters the results based on the <code>ConformancePackComplianceScoresFilters</code>.</p>"""
    sort_order: NotRequired["aws_sdk_config_service.types.sort_order.SortOrder"]
    """<p>Determines the order in which conformance pack compliance scores are sorted. Either in ascending or descending order.</p> <p>By default, conformance pack compliance scores are sorted in alphabetical order by name of the conformance pack. Conformance pack compliance scores are sorted in reverse alphabetical order if you enter <code>DESCENDING</code>.</p> <p>You can sort conformance pack compliance scores by the numerical value of the compliance score by entering <code>SCORE</code> in the <code>SortBy</code> action. When compliance scores are sorted by <code>SCORE</code>, conformance packs with a compliance score of <code>INSUFFICIENT_DATA</code> will be last when sorting by ascending order and first when sorting by descending order.</p>"""
    sort_by: NotRequired["aws_sdk_config_service.types.sort_by.SortBy"]
    """<p>Sorts your conformance pack compliance scores in either ascending or descending order, depending on <code>SortOrder</code>.</p> <p>By default, conformance pack compliance scores are sorted in alphabetical order by name of the conformance pack. Enter <code>SCORE</code>, to sort conformance pack compliance scores by the numerical value of the compliance score.</p>"""
    limit: "aws_sdk_config_service.types.page_size_limit.PageSizeLimit"
    """<p>The maximum number of conformance pack compliance scores returned on each page.</p>"""
    next_token: NotRequired["aws_sdk_config_service.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> string in a prior request that you can use to get the paginated response for the next set of conformance pack compliance scores.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListConformancePackComplianceScoresRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_config_service.types.conformance_pack_compliance_scores_filters

        out["Filters"] = (
            aws_sdk_config_service.types.conformance_pack_compliance_scores_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "sort_order" in value:
        import aws_sdk_config_service.types.sort_order

        out["SortOrder"] = (
            aws_sdk_config_service.types.sort_order.serialize_aws_json_1_1(
                value["sort_order"]
            )
        )
    if "sort_by" in value:
        import aws_sdk_config_service.types.sort_by

        out["SortBy"] = aws_sdk_config_service.types.sort_by.serialize_aws_json_1_1(
            value["sort_by"]
        )
    out["Limit"] = value.get("limit", 0)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListConformancePackComplianceScoresRequest:
    out: ListConformancePackComplianceScoresRequest = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import aws_sdk_config_service.types.conformance_pack_compliance_scores_filters

        out["filters"] = (
            aws_sdk_config_service.types.conformance_pack_compliance_scores_filters.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if "SortOrder" in data:
        import aws_sdk_config_service.types.sort_order

        out["sort_order"] = (
            aws_sdk_config_service.types.sort_order.deserialize_aws_json_1_1(
                data["SortOrder"]
            )
        )
    if "SortBy" in data:
        import aws_sdk_config_service.types.sort_by

        out["sort_by"] = aws_sdk_config_service.types.sort_by.deserialize_aws_json_1_1(
            data["SortBy"]
        )
    if "Limit" in data:
        out["limit"] = data["Limit"]
    else:
        out["limit"] = 0
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
