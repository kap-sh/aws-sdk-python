"""Generated from Smithy shape ``com.amazonaws.inspector2#ListCisScanResultsAggregatedByTargetResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.cis_scan_arn
    import aws_sdk_inspector2.types.cis_scan_results_aggregated_by_target_resource_filter_criteria
    import aws_sdk_inspector2.types.cis_scan_results_aggregated_by_target_resource_sort_by
    import aws_sdk_inspector2.types.cis_scan_results_max_results
    import aws_sdk_inspector2.types.cis_sort_order
    import aws_sdk_inspector2.types.next_token


class ListCisScanResultsAggregatedByTargetResourceRequest(TypedDict):
    scan_arn: "aws_sdk_inspector2.types.cis_scan_arn.CisScanArn"
    """<p>The scan ARN.</p>"""
    filter_criteria: NotRequired[
        "aws_sdk_inspector2.types.cis_scan_results_aggregated_by_target_resource_filter_criteria.CisScanResultsAggregatedByTargetResourceFilterCriteria"
    ]
    """<p>The filter criteria.</p>"""
    sort_by: "aws_sdk_inspector2.types.cis_scan_results_aggregated_by_target_resource_sort_by.CisScanResultsAggregatedByTargetResourceSortBy"
    """<p>The sort by order.</p>"""
    sort_order: NotRequired["aws_sdk_inspector2.types.cis_sort_order.CisSortOrder"]
    """<p>The sort order.</p>"""
    next_token: NotRequired["aws_sdk_inspector2.types.next_token.NextToken"]
    """<p>The pagination token from a previous request that's used to retrieve the next page of results.</p>"""
    max_results: (
        "aws_sdk_inspector2.types.cis_scan_results_max_results.CisScanResultsMaxResults"
    )
    """<p>The maximum number of scan results aggregated by a target resource to be returned in a single page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCisScanResultsAggregatedByTargetResourceRequest) -> dict:
    out: dict = {}
    out["scanArn"] = value["scan_arn"]
    if "filter_criteria" in value:
        import aws_sdk_inspector2.types.cis_scan_results_aggregated_by_target_resource_filter_criteria

        out["filterCriteria"] = (
            aws_sdk_inspector2.types.cis_scan_results_aggregated_by_target_resource_filter_criteria.serialize_json(
                value["filter_criteria"]
            )
        )
    import aws_sdk_inspector2.types.cis_scan_results_aggregated_by_target_resource_sort_by

    out["sortBy"] = (
        aws_sdk_inspector2.types.cis_scan_results_aggregated_by_target_resource_sort_by.serialize_json(
            value.get("sort_by", "FAILED_COUNTS")
        )
    )
    if "sort_order" in value:
        import aws_sdk_inspector2.types.cis_sort_order

        out["sortOrder"] = aws_sdk_inspector2.types.cis_sort_order.serialize_json(
            value["sort_order"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    out["maxResults"] = value.get("max_results", 100)
    return out


def deserialize_json(data: dict) -> ListCisScanResultsAggregatedByTargetResourceRequest:
    out: ListCisScanResultsAggregatedByTargetResourceRequest = {}  # type: ignore[typeddict-item]
    if "scanArn" in data:
        out["scan_arn"] = data["scanArn"]
    else:
        raise DeserializationError(
            "ListCisScanResultsAggregatedByTargetResourceRequest.scan_arn required"
        )
    if "filterCriteria" in data:
        import aws_sdk_inspector2.types.cis_scan_results_aggregated_by_target_resource_filter_criteria

        out["filter_criteria"] = (
            aws_sdk_inspector2.types.cis_scan_results_aggregated_by_target_resource_filter_criteria.deserialize_json(
                data["filterCriteria"]
            )
        )
    if "sortBy" in data:
        import aws_sdk_inspector2.types.cis_scan_results_aggregated_by_target_resource_sort_by

        out["sort_by"] = (
            aws_sdk_inspector2.types.cis_scan_results_aggregated_by_target_resource_sort_by.deserialize_json(
                data["sortBy"]
            )
        )
    else:
        out["sort_by"] = "FAILED_COUNTS"
    if "sortOrder" in data:
        import aws_sdk_inspector2.types.cis_sort_order

        out["sort_order"] = aws_sdk_inspector2.types.cis_sort_order.deserialize_json(
            data["sortOrder"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    else:
        out["max_results"] = 100
    return out
