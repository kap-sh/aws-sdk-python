"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#ListWorkloadEstimateUsageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.next_page_token
    import capo_bcm_pricing_calculator.types.workload_estimate_usage_items


class ListWorkloadEstimateUsageResponse(TypedDict, closed=True):
    items: NotRequired[
        "capo_bcm_pricing_calculator.types.workload_estimate_usage_items.WorkloadEstimateUsageItems"
    ]
    """<p> The list of usage items associated with the workload estimate. </p>"""
    next_token: NotRequired[
        "capo_bcm_pricing_calculator.types.next_page_token.NextPageToken"
    ]
    """<p> A token to retrieve the next page of results, if any. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListWorkloadEstimateUsageResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_bcm_pricing_calculator.types.workload_estimate_usage_items

        out["items"] = (
            capo_bcm_pricing_calculator.types.workload_estimate_usage_items.serialize_aws_json_1_0(
                value["items"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListWorkloadEstimateUsageResponse:
    out: ListWorkloadEstimateUsageResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import capo_bcm_pricing_calculator.types.workload_estimate_usage_items

        out["items"] = (
            capo_bcm_pricing_calculator.types.workload_estimate_usage_items.deserialize_aws_json_1_0(
                data["items"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
