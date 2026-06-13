"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#RecurringPaymentTerm``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.billing_period_type
    import aws_sdk_marketplace_discovery.types.bounded_string
    import aws_sdk_marketplace_discovery.types.currency_code
    import aws_sdk_marketplace_discovery.types.term_id
    import aws_sdk_marketplace_discovery.types.term_type


class RecurringPaymentTerm(TypedDict):
    id: "aws_sdk_marketplace_discovery.types.term_id.TermId"
    """<p>The unique identifier of the term.</p>"""
    type: "aws_sdk_marketplace_discovery.types.term_type.TermType"
    """<p>The category of the term.</p>"""
    currency_code: "aws_sdk_marketplace_discovery.types.currency_code.CurrencyCode"
    """<p>Defines the currency for the prices in this term.</p>"""
    billing_period: (
        "aws_sdk_marketplace_discovery.types.billing_period_type.BillingPeriodType"
    )
    """<p>The billing period frequency, such as <code>Monthly</code>.</p>"""
    price: "aws_sdk_marketplace_discovery.types.bounded_string.BoundedString"
    """<p>The amount charged each billing period.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecurringPaymentTerm) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import aws_sdk_marketplace_discovery.types.term_type

    out["type"] = aws_sdk_marketplace_discovery.types.term_type.serialize_json(
        value["type"]
    )
    out["currencyCode"] = value["currency_code"]
    import aws_sdk_marketplace_discovery.types.billing_period_type

    out["billingPeriod"] = (
        aws_sdk_marketplace_discovery.types.billing_period_type.serialize_json(
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
        import aws_sdk_marketplace_discovery.types.term_type

        out["type"] = aws_sdk_marketplace_discovery.types.term_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("RecurringPaymentTerm.type required")
    if "currencyCode" in data:
        out["currency_code"] = data["currencyCode"]
    else:
        raise DeserializationError("RecurringPaymentTerm.currency_code required")
    if "billingPeriod" in data:
        import aws_sdk_marketplace_discovery.types.billing_period_type

        out["billing_period"] = (
            aws_sdk_marketplace_discovery.types.billing_period_type.deserialize_json(
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
