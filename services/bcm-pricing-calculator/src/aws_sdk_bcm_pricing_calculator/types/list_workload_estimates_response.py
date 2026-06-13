"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#ListWorkloadEstimatesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.next_page_token
    import aws_sdk_bcm_pricing_calculator.types.workload_estimate_summaries


class ListWorkloadEstimatesResponse(TypedDict):
    items: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.workload_estimate_summaries.WorkloadEstimateSummaries"
    ]
    """<p> The list of workload estimates for the account. </p>"""
    next_token: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.next_page_token.NextPageToken"
    ]
    """<p> A token to retrieve the next page of results, if any. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListWorkloadEstimatesResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_bcm_pricing_calculator.types.workload_estimate_summaries

        out["items"] = (
            aws_sdk_bcm_pricing_calculator.types.workload_estimate_summaries.serialize_aws_json_1_0(
                value["items"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListWorkloadEstimatesResponse:
    out: ListWorkloadEstimatesResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_bcm_pricing_calculator.types.workload_estimate_summaries

        out["items"] = (
            aws_sdk_bcm_pricing_calculator.types.workload_estimate_summaries.deserialize_aws_json_1_0(
                data["items"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
