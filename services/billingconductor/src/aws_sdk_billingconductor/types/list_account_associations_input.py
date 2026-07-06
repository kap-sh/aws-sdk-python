"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListAccountAssociationsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.billing_period
    import aws_sdk_billingconductor.types.list_account_associations_filter
    import aws_sdk_billingconductor.types.token


class ListAccountAssociationsInput(TypedDict, closed=True):
    billing_period: NotRequired[
        "aws_sdk_billingconductor.types.billing_period.BillingPeriod"
    ]
    """<p> The preferred billing period to get account associations. </p>"""
    filters: NotRequired[
        "aws_sdk_billingconductor.types.list_account_associations_filter.ListAccountAssociationsFilter"
    ]
    """<p>The filter on the account ID of the linked account, or any of the following:</p> <p> <code>MONITORED</code>: linked accounts that are associated to billing groups.</p> <p> <code>UNMONITORED</code>: linked accounts that aren't associated to billing groups.</p> <p> <code>Billing Group Arn</code>: linked accounts that are associated to the provided billing group Arn. </p>"""
    next_token: NotRequired["aws_sdk_billingconductor.types.token.Token"]
    """<p> The pagination token that's used on subsequent calls to retrieve accounts. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAccountAssociationsInput) -> dict:
    out: dict = {}
    if "billing_period" in value:
        out["BillingPeriod"] = value["billing_period"]
    if "filters" in value:
        import aws_sdk_billingconductor.types.list_account_associations_filter

        out["Filters"] = (
            aws_sdk_billingconductor.types.list_account_associations_filter.serialize_json(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAccountAssociationsInput:
    out: ListAccountAssociationsInput = {}  # type: ignore[typeddict-item]
    if "BillingPeriod" in data:
        out["billing_period"] = data["BillingPeriod"]
    if "Filters" in data:
        import aws_sdk_billingconductor.types.list_account_associations_filter

        out["filters"] = (
            aws_sdk_billingconductor.types.list_account_associations_filter.deserialize_json(
                data["Filters"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
