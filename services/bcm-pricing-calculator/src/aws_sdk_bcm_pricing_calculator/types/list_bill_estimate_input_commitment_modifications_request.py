"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#ListBillEstimateInputCommitmentModificationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bcm_pricing_calculator.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.max_results
    import aws_sdk_bcm_pricing_calculator.types.next_page_token
    import aws_sdk_bcm_pricing_calculator.types.resource_id


class ListBillEstimateInputCommitmentModificationsRequest(TypedDict, closed=True):
    bill_estimate_id: "aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId"
    """<p> The unique identifier of the bill estimate to list input commitment modifications for. </p>"""
    next_token: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.next_page_token.NextPageToken"
    ]
    """<p> A token to retrieve the next page of results. </p>"""
    max_results: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.max_results.MaxResults"
    ]
    """<p> The maximum number of results to return per page. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: ListBillEstimateInputCommitmentModificationsRequest,
) -> dict:
    out: dict = {}
    out["billEstimateId"] = value["bill_estimate_id"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> ListBillEstimateInputCommitmentModificationsRequest:
    out: ListBillEstimateInputCommitmentModificationsRequest = {}  # type: ignore[typeddict-item]
    if "billEstimateId" in data:
        out["bill_estimate_id"] = data["billEstimateId"]
    else:
        raise DeserializationError(
            "ListBillEstimateInputCommitmentModificationsRequest.bill_estimate_id required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
