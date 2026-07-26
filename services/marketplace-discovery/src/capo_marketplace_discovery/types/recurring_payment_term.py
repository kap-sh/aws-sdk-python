"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#RecurringPaymentTerm``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.billing_period_type
    import capo_marketplace_discovery.types.bounded_string
    import capo_marketplace_discovery.types.currency_code
    import capo_marketplace_discovery.types.term_id
    import capo_marketplace_discovery.types.term_type


class RecurringPaymentTerm(TypedDict, closed=True):
    id: "capo_marketplace_discovery.types.term_id.TermId"
    """<p>The unique identifier of the term.</p>"""
    type: "capo_marketplace_discovery.types.term_type.TermType"
    """<p>The category of the term.</p>"""
    currency_code: "capo_marketplace_discovery.types.currency_code.CurrencyCode"
    """<p>Defines the currency for the prices in this term.</p>"""
    billing_period: (
        "capo_marketplace_discovery.types.billing_period_type.BillingPeriodType"
    )
    """<p>The billing period frequency, such as <code>Monthly</code>.</p>"""
    price: "capo_marketplace_discovery.types.bounded_string.BoundedString"
    """<p>The amount charged each billing period.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecurringPaymentTerm) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import capo_marketplace_discovery.types.term_type

    out["type"] = capo_marketplace_discovery.types.term_type.serialize_json(
        value["type"]
    )
    out["currencyCode"] = value["currency_code"]
    import capo_marketplace_discovery.types.billing_period_type

    out["billingPeriod"] = (
        capo_marketplace_discovery.types.billing_period_type.serialize_json(
            value["billing_period"]
        )
    )
    out["price"] = value["price"]
    return out


def deserialize_json(data: dict) -> RecurringPaymentTerm:
    out: RecurringPaymentTerm = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("RecurringPaymentTerm.id required")
    if "type" in data:
        import capo_marketplace_discovery.types.term_type

        out["type"] = capo_marketplace_discovery.types.term_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("RecurringPaymentTerm.type required")
    if "currencyCode" in data:
        out["currency_code"] = data["currencyCode"]
    else:
        raise DeserializationError("RecurringPaymentTerm.currency_code required")
    if "billingPeriod" in data:
        import capo_marketplace_discovery.types.billing_period_type

        out["billing_period"] = (
            capo_marketplace_discovery.types.billing_period_type.deserialize_json(
                data["billingPeriod"]
            )
        )
    else:
        raise DeserializationError("RecurringPaymentTerm.billing_period required")
    if "price" in data:
        out["price"] = data["price"]
    else:
        raise DeserializationError("RecurringPaymentTerm.price required")
    return out
