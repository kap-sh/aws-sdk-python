"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#ListBillScenariosRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.filter_timestamp
    import aws_sdk_bcm_pricing_calculator.types.list_bill_scenarios_filters
    import aws_sdk_bcm_pricing_calculator.types.max_results
    import aws_sdk_bcm_pricing_calculator.types.next_page_token


class ListBillScenariosRequest(TypedDict):
    filters: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.list_bill_scenarios_filters.ListBillScenariosFilters"
    ]
    """<p> Filters to apply to the list of bill scenarios. </p>"""
    created_at_filter: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.filter_timestamp.FilterTimestamp"
    ]
    """<p> Filter bill scenarios based on the creation date. </p>"""
    expires_at_filter: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.filter_timestamp.FilterTimestamp"
    ]
    """<p> Filter bill scenarios based on the expiration date. </p>"""
    next_token: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.next_page_token.NextPageToken"
    ]
    """<p> A token to retrieve the next page of results. </p>"""
    max_results: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.max_results.MaxResults"
    ]
    """<p> The maximum number of results to return per page. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListBillScenariosRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_bcm_pricing_calculator.types.list_bill_scenarios_filters

        out["filters"] = (
            aws_sdk_bcm_pricing_calculator.types.list_bill_scenarios_filters.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    if "created_at_filter" in value:
        import aws_sdk_bcm_pricing_calculator.types.filter_timestamp

        out["createdAtFilter"] = (
            aws_sdk_bcm_pricing_calculator.types.filter_timestamp.serialize_aws_json_1_0(
                value["created_at_filter"]
            )
        )
    if "expires_at_filter" in value:
        import aws_sdk_bcm_pricing_calculator.types.filter_timestamp

        out["expiresAtFilter"] = (
            aws_sdk_bcm_pricing_calculator.types.filter_timestamp.serialize_aws_json_1_0(
                value["expires_at_filter"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListBillScenariosRequest:
    out: ListBillScenariosRequest = {}  # type: ignore[typeddict-item]
    if "filters" in data:
        import aws_sdk_bcm_pricing_calculator.types.list_bill_scenarios_filters

        out["filters"] = (
            aws_sdk_bcm_pricing_calculator.types.list_bill_scenarios_filters.deserialize_aws_json_1_0(
                data["filters"]
            )
        )
    if "createdAtFilter" in data:
        import aws_sdk_bcm_pricing_calculator.types.filter_timestamp

        out["created_at_filter"] = (
            aws_sdk_bcm_pricing_calculator.types.filter_timestamp.deserialize_aws_json_1_0(
                data["createdAtFilter"]
            )
        )
    if "expiresAtFilter" in data:
        import aws_sdk_bcm_pricing_calculator.types.filter_timestamp

        out["expires_at_filter"] = (
            aws_sdk_bcm_pricing_calculator.types.filter_timestamp.deserialize_aws_json_1_0(
                data["expiresAtFilter"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
