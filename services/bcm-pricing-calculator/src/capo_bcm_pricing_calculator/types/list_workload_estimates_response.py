"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#ListWorkloadEstimatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.next_page_token
    import capo_bcm_pricing_calculator.types.workload_estimate_summaries


class ListWorkloadEstimatesResponse(TypedDict, closed=True):
    items: NotRequired[
        "capo_bcm_pricing_calculator.types.workload_estimate_summaries.WorkloadEstimateSummaries"
    ]
    """<p> The list of workload estimates for the account. </p>"""
    next_token: NotRequired[
        "capo_bcm_pricing_calculator.types.next_page_token.NextPageToken"
    ]
    """<p> A token to retrieve the next page of results, if any. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListWorkloadEstimatesResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_bcm_pricing_calculator.types.workload_estimate_summaries

        out["items"] = (
            capo_bcm_pricing_calculator.types.workload_estimate_summaries.serialize_aws_json_1_0(
                value["items"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListWorkloadEstimatesResponse:
    out: ListWorkloadEstimatesResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import capo_bcm_pricing_calculator.types.workload_estimate_summaries

        out["items"] = (
            capo_bcm_pricing_calculator.types.workload_estimate_summaries.deserialize_aws_json_1_0(
                data["items"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
