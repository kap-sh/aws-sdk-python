"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#ListBillEstimatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.bill_estimate_summaries
    import aws_sdk_bcm_pricing_calculator.types.next_page_token


class ListBillEstimatesResponse(TypedDict, closed=True):
    items: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.bill_estimate_summaries.BillEstimateSummaries"
    ]
    """<p> The list of bill estimates for the account. </p>"""
    next_token: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.next_page_token.NextPageToken"
    ]
    """<p> A token to retrieve the next page of results, if any. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListBillEstimatesResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_bcm_pricing_calculator.types.bill_estimate_summaries

        out["items"] = (
            aws_sdk_bcm_pricing_calculator.types.bill_estimate_summaries.serialize_aws_json_1_0(
                value["items"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListBillEstimatesResponse:
    out: ListBillEstimatesResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_bcm_pricing_calculator.types.bill_estimate_summaries

        out["items"] = (
            aws_sdk_bcm_pricing_calculator.types.bill_estimate_summaries.deserialize_aws_json_1_0(
                data["items"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
