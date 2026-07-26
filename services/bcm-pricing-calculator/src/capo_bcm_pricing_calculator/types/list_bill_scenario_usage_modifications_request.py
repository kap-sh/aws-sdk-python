"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#ListBillScenarioUsageModificationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bcm_pricing_calculator.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.list_usage_filters
    import capo_bcm_pricing_calculator.types.max_results
    import capo_bcm_pricing_calculator.types.next_page_token
    import capo_bcm_pricing_calculator.types.resource_id


class ListBillScenarioUsageModificationsRequest(TypedDict, closed=True):
    bill_scenario_id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId"
    """<p> The unique identifier of the bill scenario to list usage modifications for. </p>"""
    filters: NotRequired[
        "capo_bcm_pricing_calculator.types.list_usage_filters.ListUsageFilters"
    ]
    """<p> Filters to apply to the list of usage modifications. </p>"""
    next_token: NotRequired[
        "capo_bcm_pricing_calculator.types.next_page_token.NextPageToken"
    ]
    """<p> A token to retrieve the next page of results. </p>"""
    max_results: NotRequired["capo_bcm_pricing_calculator.types.max_results.MaxResults"]
    """<p> The maximum number of results to return per page. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListBillScenarioUsageModificationsRequest) -> dict:
    out: dict = {}
    out["billScenarioId"] = value["bill_scenario_id"]
    if "filters" in value:
        import capo_bcm_pricing_calculator.types.list_usage_filters

        out["filters"] = (
            capo_bcm_pricing_calculator.types.list_usage_filters.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListBillScenarioUsageModificationsRequest:
    out: ListBillScenarioUsageModificationsRequest = {}  # type: ignore[typeddict-item]
    if "billScenarioId" in data:
        out["bill_scenario_id"] = data["billScenarioId"]
    else:
        raise DeserializationError(
            "ListBillScenarioUsageModificationsRequest.bill_scenario_id required"
        )
    if "filters" in data:
        import capo_bcm_pricing_calculator.types.list_usage_filters

        out["filters"] = (
            capo_bcm_pricing_calculator.types.list_usage_filters.deserialize_aws_json_1_0(
                data["filters"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
