"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListCustomLineItemVersionsFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.list_custom_line_item_versions_billing_period_range_filter


class ListCustomLineItemVersionsFilter(TypedDict, closed=True):
    billing_period_range: NotRequired[
        "aws_sdk_billingconductor.types.list_custom_line_item_versions_billing_period_range_filter.ListCustomLineItemVersionsBillingPeriodRangeFilter"
    ]
    """<p>The billing period range in which the custom line item version is applied.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCustomLineItemVersionsFilter) -> dict:
    out: dict = {}
    if "billing_period_range" in value:
        import aws_sdk_billingconductor.types.list_custom_line_item_versions_billing_period_range_filter

        out["BillingPeriodRange"] = (
            aws_sdk_billingconductor.types.list_custom_line_item_versions_billing_period_range_filter.serialize_json(
                value["billing_period_range"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListCustomLineItemVersionsFilter:
    out: ListCustomLineItemVersionsFilter = {}  # type: ignore[typeddict-item]
    if "BillingPeriodRange" in data:
        import aws_sdk_billingconductor.types.list_custom_line_item_versions_billing_period_range_filter

        out["billing_period_range"] = (
            aws_sdk_billingconductor.types.list_custom_line_item_versions_billing_period_range_filter.deserialize_json(
                data["BillingPeriodRange"]
            )
        )
    return out
