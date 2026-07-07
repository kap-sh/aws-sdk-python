"""Generated from Smithy shape ``com.amazonaws.billing#ListBillingViewsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_billing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_billing.types.billing_view_list
    import aws_sdk_billing.types.page_token


class ListBillingViewsResponse(TypedDict, closed=True):
    billing_views: "aws_sdk_billing.types.billing_view_list.BillingViewList"
    """<p>A list of <code>BillingViewListElement</code> retrieved.</p>"""
    next_token: NotRequired["aws_sdk_billing.types.page_token.PageToken"]
    """<p>The pagination token to use on subsequent calls to list billing views. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListBillingViewsResponse) -> dict:
    out: dict = {}
    import aws_sdk_billing.types.billing_view_list

    out["billingViews"] = (
        aws_sdk_billing.types.billing_view_list.serialize_aws_json_1_0(
            value["billing_views"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListBillingViewsResponse:
    out: ListBillingViewsResponse = {}  # type: ignore[typeddict-item]
    if "billingViews" in data:
        import aws_sdk_billing.types.billing_view_list

        out["billing_views"] = (
            aws_sdk_billing.types.billing_view_list.deserialize_aws_json_1_0(
                data["billingViews"]
            )
        )
    else:
        raise DeserializationError("ListBillingViewsResponse.billing_views required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
