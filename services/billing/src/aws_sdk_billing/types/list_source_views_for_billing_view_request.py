"""Generated from Smithy shape ``com.amazonaws.billing#ListSourceViewsForBillingViewRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_billing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_billing.types.billing_view_arn
    import aws_sdk_billing.types.billing_views_max_results
    import aws_sdk_billing.types.page_token


class ListSourceViewsForBillingViewRequest(TypedDict, closed=True):
    arn: "aws_sdk_billing.types.billing_view_arn.BillingViewArn"
    """<p> The Amazon Resource Name (ARN) that can be used to uniquely identify the billing view. </p>"""
    max_results: NotRequired[
        "aws_sdk_billing.types.billing_views_max_results.BillingViewsMaxResults"
    ]
    """<p> The number of entries a paginated response contains. </p>"""
    next_token: NotRequired["aws_sdk_billing.types.page_token.PageToken"]
    """<p> The pagination token that is used on subsequent calls to list billing views. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListSourceViewsForBillingViewRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListSourceViewsForBillingViewRequest:
    out: ListSourceViewsForBillingViewRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ListSourceViewsForBillingViewRequest.arn required")
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
