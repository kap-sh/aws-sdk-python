"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListCustomLineItemVersionsBillingPeriodRangeFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.billing_period


class ListCustomLineItemVersionsBillingPeriodRangeFilter(TypedDict, closed=True):
    start_billing_period: NotRequired[
        "capo_billingconductor.types.billing_period.BillingPeriod"
    ]
    """<p>The inclusive start billing period that defines a billing period range where a custom line item version is applied.</p>"""
    end_billing_period: NotRequired[
        "capo_billingconductor.types.billing_period.BillingPeriod"
    ]
    """<p>The exclusive end billing period that defines a billing period range where a custom line item version is applied.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCustomLineItemVersionsBillingPeriodRangeFilter) -> dict:
    out: dict = {}
    if "start_billing_period" in value:
        out["StartBillingPeriod"] = value["start_billing_period"]
    if "end_billing_period" in value:
        out["EndBillingPeriod"] = value["end_billing_period"]
    return out


def deserialize_json(data: dict) -> ListCustomLineItemVersionsBillingPeriodRangeFilter:
    out: ListCustomLineItemVersionsBillingPeriodRangeFilter = {}  # type: ignore[typeddict-item]
    if "StartBillingPeriod" in data:
        out["start_billing_period"] = data["StartBillingPeriod"]
    if "EndBillingPeriod" in data:
        out["end_billing_period"] = data["EndBillingPeriod"]
    return out
