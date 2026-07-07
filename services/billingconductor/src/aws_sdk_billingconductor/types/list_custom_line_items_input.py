"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListCustomLineItemsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.billing_period
    import aws_sdk_billingconductor.types.list_custom_line_items_filter
    import aws_sdk_billingconductor.types.max_custom_line_item_results
    import aws_sdk_billingconductor.types.token


class ListCustomLineItemsInput(TypedDict, closed=True):
    billing_period: NotRequired[
        "aws_sdk_billingconductor.types.billing_period.BillingPeriod"
    ]
    """<p> The preferred billing period to get custom line items (FFLIs). </p>"""
    max_results: NotRequired[
        "aws_sdk_billingconductor.types.max_custom_line_item_results.MaxCustomLineItemResults"
    ]
    """<p> The maximum number of billing groups to retrieve. </p>"""
    next_token: NotRequired["aws_sdk_billingconductor.types.token.Token"]
    """<p> The pagination token that's used on subsequent calls to get custom line items (FFLIs). </p>"""
    filters: NotRequired[
        "aws_sdk_billingconductor.types.list_custom_line_items_filter.ListCustomLineItemsFilter"
    ]
    """<p>A <code>ListCustomLineItemsFilter</code> that specifies the custom line item names and/or billing group Amazon Resource Names (ARNs) to retrieve FFLI information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCustomLineItemsInput) -> dict:
    out: dict = {}
    if "billing_period" in value:
        out["BillingPeriod"] = value["billing_period"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "filters" in value:
        import aws_sdk_billingconductor.types.list_custom_line_items_filter

        out["Filters"] = (
            aws_sdk_billingconductor.types.list_custom_line_items_filter.serialize_json(
                value["filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListCustomLineItemsInput:
    out: ListCustomLineItemsInput = {}  # type: ignore[typeddict-item]
    if "BillingPeriod" in data:
        out["billing_period"] = data["BillingPeriod"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Filters" in data:
        import aws_sdk_billingconductor.types.list_custom_line_items_filter

        out["filters"] = (
            aws_sdk_billingconductor.types.list_custom_line_items_filter.deserialize_json(
                data["Filters"]
            )
        )
    return out
