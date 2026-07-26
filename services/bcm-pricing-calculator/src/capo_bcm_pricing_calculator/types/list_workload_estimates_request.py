"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#ListWorkloadEstimatesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.filter_timestamp
    import capo_bcm_pricing_calculator.types.list_workload_estimates_filters
    import capo_bcm_pricing_calculator.types.max_results
    import capo_bcm_pricing_calculator.types.next_page_token


class ListWorkloadEstimatesRequest(TypedDict, closed=True):
    created_at_filter: NotRequired[
        "capo_bcm_pricing_calculator.types.filter_timestamp.FilterTimestamp"
    ]
    """<p> Filter workload estimates based on the creation date. </p>"""
    expires_at_filter: NotRequired[
        "capo_bcm_pricing_calculator.types.filter_timestamp.FilterTimestamp"
    ]
    """<p> Filter workload estimates based on the expiration date. </p>"""
    filters: NotRequired[
        "capo_bcm_pricing_calculator.types.list_workload_estimates_filters.ListWorkloadEstimatesFilters"
    ]
    """<p> Filters to apply to the list of workload estimates. </p>"""
    next_token: NotRequired[
        "capo_bcm_pricing_calculator.types.next_page_token.NextPageToken"
    ]
    """<p> A token to retrieve the next page of results. </p>"""
    max_results: NotRequired["capo_bcm_pricing_calculator.types.max_results.MaxResults"]
    """<p> The maximum number of results to return per page. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListWorkloadEstimatesRequest) -> dict:
    out: dict = {}
    if "created_at_filter" in value:
        import capo_bcm_pricing_calculator.types.filter_timestamp

        out["createdAtFilter"] = (
            capo_bcm_pricing_calculator.types.filter_timestamp.serialize_aws_json_1_0(
                value["created_at_filter"]
            )
        )
    if "expires_at_filter" in value:
        import capo_bcm_pricing_calculator.types.filter_timestamp

        out["expiresAtFilter"] = (
            capo_bcm_pricing_calculator.types.filter_timestamp.serialize_aws_json_1_0(
                value["expires_at_filter"]
            )
        )
    if "filters" in value:
        import capo_bcm_pricing_calculator.types.list_workload_estimates_filters

        out["filters"] = (
            capo_bcm_pricing_calculator.types.list_workload_estimates_filters.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListWorkloadEstimatesRequest:
    out: ListWorkloadEstimatesRequest = {}  # type: ignore[typeddict-item]
    if "createdAtFilter" in data:
        import capo_bcm_pricing_calculator.types.filter_timestamp

        out["created_at_filter"] = (
            capo_bcm_pricing_calculator.types.filter_timestamp.deserialize_aws_json_1_0(
                data["createdAtFilter"]
            )
        )
    if "expiresAtFilter" in data:
        import capo_bcm_pricing_calculator.types.filter_timestamp

        out["expires_at_filter"] = (
            capo_bcm_pricing_calculator.types.filter_timestamp.deserialize_aws_json_1_0(
                data["expiresAtFilter"]
            )
        )
    if "filters" in data:
        import capo_bcm_pricing_calculator.types.list_workload_estimates_filters

        out["filters"] = (
            capo_bcm_pricing_calculator.types.list_workload_estimates_filters.deserialize_aws_json_1_0(
                data["filters"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
