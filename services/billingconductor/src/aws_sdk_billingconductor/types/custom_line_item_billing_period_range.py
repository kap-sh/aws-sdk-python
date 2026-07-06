"""Generated from Smithy shape ``com.amazonaws.billingconductor#CustomLineItemBillingPeriodRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_billingconductor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.billing_period


class CustomLineItemBillingPeriodRange(TypedDict, closed=True):
    inclusive_start_billing_period: (
        "aws_sdk_billingconductor.types.billing_period.BillingPeriod"
    )
    """<p>The inclusive start billing period that defines a billing period range where a custom line is applied.</p>"""
    exclusive_end_billing_period: NotRequired[
        "aws_sdk_billingconductor.types.billing_period.BillingPeriod"
    ]
    """<p>The inclusive end billing period that defines a billing period range where a custom line is applied.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomLineItemBillingPeriodRange) -> dict:
    out: dict = {}
    out["InclusiveStartBillingPeriod"] = value["inclusive_start_billing_period"]
    if "exclusive_end_billing_period" in value:
        out["ExclusiveEndBillingPeriod"] = value["exclusive_end_billing_period"]
    return out


def deserialize_json(data: dict) -> CustomLineItemBillingPeriodRange:
    out: CustomLineItemBillingPeriodRange = {}  # type: ignore[typeddict-item]
    if "InclusiveStartBillingPeriod" in data:
        out["inclusive_start_billing_period"] = data["InclusiveStartBillingPeriod"]
    else:
        raise DeserializationError(
            "CustomLineItemBillingPeriodRange.inclusive_start_billing_period required"
        )
    if "ExclusiveEndBillingPeriod" in data:
        out["exclusive_end_billing_period"] = data["ExclusiveEndBillingPeriod"]
    return out
