"""Generated from Smithy shape ``com.amazonaws.outposts#SubscriptionPricingDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_outposts.types.currency_code
    import aws_sdk_outposts.types.nullable_float
    import aws_sdk_outposts.types.payment_option
    import aws_sdk_outposts.types.payment_term


class SubscriptionPricingDetails(TypedDict, closed=True):
    payment_option: NotRequired["aws_sdk_outposts.types.payment_option.PaymentOption"]
    """<p>The payment option.</p>"""
    payment_term: NotRequired["aws_sdk_outposts.types.payment_term.PaymentTerm"]
    """<p>The payment term.</p>"""
    upfront_price: NotRequired["aws_sdk_outposts.types.nullable_float.NullableFloat"]
    """<p>The upfront price.</p>"""
    monthly_recurring_price: NotRequired[
        "aws_sdk_outposts.types.nullable_float.NullableFloat"
    ]
    """<p>The monthly recurring price.</p>"""
    currency: NotRequired["aws_sdk_outposts.types.currency_code.CurrencyCode"]
    """<p>The currency of the price. Currently only <code>USD</code> is supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionPricingDetails) -> dict:
    out: dict = {}
    if "payment_option" in value:
        import aws_sdk_outposts.types.payment_option

        out["PaymentOption"] = aws_sdk_outposts.types.payment_option.serialize_json(
            value["payment_option"]
        )
    if "payment_term" in value:
        import aws_sdk_outposts.types.payment_term

        out["PaymentTerm"] = aws_sdk_outposts.types.payment_term.serialize_json(
            value["payment_term"]
        )
    if "upfront_price" in value:
        out["UpfrontPrice"] = value["upfront_price"]
    if "monthly_recurring_price" in value:
        out["MonthlyRecurringPrice"] = value["monthly_recurring_price"]
    if "currency" in value:
        import aws_sdk_outposts.types.currency_code

        out["Currency"] = aws_sdk_outposts.types.currency_code.serialize_json(
            value["currency"]
        )
    return out


def deserialize_json(data: dict) -> SubscriptionPricingDetails:
    out: SubscriptionPricingDetails = {}  # type: ignore[typeddict-item]
    if "PaymentOption" in data:
        import aws_sdk_outposts.types.payment_option

        out["payment_option"] = aws_sdk_outposts.types.payment_option.deserialize_json(
            data["PaymentOption"]
        )
    if "PaymentTerm" in data:
        import aws_sdk_outposts.types.payment_term

        out["payment_term"] = aws_sdk_outposts.types.payment_term.deserialize_json(
            data["PaymentTerm"]
        )
    if "UpfrontPrice" in data:
        out["upfront_price"] = data["UpfrontPrice"]
    if "MonthlyRecurringPrice" in data:
        out["monthly_recurring_price"] = data["MonthlyRecurringPrice"]
    if "Currency" in data:
        import aws_sdk_outposts.types.currency_code

        out["currency"] = aws_sdk_outposts.types.currency_code.deserialize_json(
            data["Currency"]
        )
    return out
