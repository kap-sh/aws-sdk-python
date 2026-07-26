"""Generated from Smithy shape ``com.amazonaws.outposts#CreateRenewalOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.currency_code
    import capo_outposts.types.nullable_float
    import capo_outposts.types.outpost_id_only
    import capo_outposts.types.payment_option
    import capo_outposts.types.payment_term


class CreateRenewalOutput(TypedDict, closed=True):
    payment_option: NotRequired["capo_outposts.types.payment_option.PaymentOption"]
    """<p>The payment option.</p>"""
    payment_term: NotRequired["capo_outposts.types.payment_term.PaymentTerm"]
    """<p>The payment term.</p>"""
    outpost_id: NotRequired["capo_outposts.types.outpost_id_only.OutpostIdOnly"]
    """<p>The ID of the Outpost.</p>"""
    upfront_price: NotRequired["capo_outposts.types.nullable_float.NullableFloat"]
    """<p>The upfront price of the renewal.</p>"""
    monthly_recurring_price: NotRequired[
        "capo_outposts.types.nullable_float.NullableFloat"
    ]
    """<p>The monthly recurring price of the renewal.</p>"""
    currency: NotRequired["capo_outposts.types.currency_code.CurrencyCode"]
    """<p>The currency of the renewal price.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRenewalOutput) -> dict:
    out: dict = {}
    if "payment_option" in value:
        import capo_outposts.types.payment_option

        out["PaymentOption"] = capo_outposts.types.payment_option.serialize_json(
            value["payment_option"]
        )
    if "payment_term" in value:
        import capo_outposts.types.payment_term

        out["PaymentTerm"] = capo_outposts.types.payment_term.serialize_json(
            value["payment_term"]
        )
    if "outpost_id" in value:
        out["OutpostId"] = value["outpost_id"]
    if "upfront_price" in value:
        out["UpfrontPrice"] = value["upfront_price"]
    if "monthly_recurring_price" in value:
        out["MonthlyRecurringPrice"] = value["monthly_recurring_price"]
    if "currency" in value:
        import capo_outposts.types.currency_code

        out["Currency"] = capo_outposts.types.currency_code.serialize_json(
            value["currency"]
        )
    return out


def deserialize_json(data: dict) -> CreateRenewalOutput:
    out: CreateRenewalOutput = {}  # type: ignore[typeddict-item]
    if "PaymentOption" in data:
        import capo_outposts.types.payment_option

        out["payment_option"] = capo_outposts.types.payment_option.deserialize_json(
            data["PaymentOption"]
        )
    if "PaymentTerm" in data:
        import capo_outposts.types.payment_term

        out["payment_term"] = capo_outposts.types.payment_term.deserialize_json(
            data["PaymentTerm"]
        )
    if "OutpostId" in data:
        out["outpost_id"] = data["OutpostId"]
    if "UpfrontPrice" in data:
        out["upfront_price"] = data["UpfrontPrice"]
    if "MonthlyRecurringPrice" in data:
        out["monthly_recurring_price"] = data["MonthlyRecurringPrice"]
    if "Currency" in data:
        import capo_outposts.types.currency_code

        out["currency"] = capo_outposts.types.currency_code.deserialize_json(
            data["Currency"]
        )
    return out
