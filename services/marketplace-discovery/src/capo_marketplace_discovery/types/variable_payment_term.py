"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#VariablePaymentTerm``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.bounded_string
    import capo_marketplace_discovery.types.currency_code
    import capo_marketplace_discovery.types.term_id
    import capo_marketplace_discovery.types.term_type


class VariablePaymentTerm(TypedDict, closed=True):
    id: "capo_marketplace_discovery.types.term_id.TermId"
    """<p>The unique identifier of the term.</p>"""
    type: "capo_marketplace_discovery.types.term_type.TermType"
    """<p>The category of the term.</p>"""
    currency_code: "capo_marketplace_discovery.types.currency_code.CurrencyCode"
    """<p>Defines the currency for the prices in this term.</p>"""
    max_total_charge_amount: (
        "capo_marketplace_discovery.types.bounded_string.BoundedString"
    )
    """<p>The maximum total amount that can be charged under this term.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VariablePaymentTerm) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import capo_marketplace_discovery.types.term_type

    out["type"] = capo_marketplace_discovery.types.term_type.serialize_json(
        value["type"]
    )
    out["currencyCode"] = value["currency_code"]
    out["maxTotalChargeAmount"] = value["max_total_charge_amount"]
    return out


def deserialize_json(data: dict) -> VariablePaymentTerm:
    out: VariablePaymentTerm = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("VariablePaymentTerm.id required")
    if "type" in data:
        import capo_marketplace_discovery.types.term_type

        out["type"] = capo_marketplace_discovery.types.term_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("VariablePaymentTerm.type required")
    if "currencyCode" in data:
        out["currency_code"] = data["currencyCode"]
    else:
        raise DeserializationError("VariablePaymentTerm.currency_code required")
    if "maxTotalChargeAmount" in data:
        out["max_total_charge_amount"] = data["maxTotalChargeAmount"]
    else:
        raise DeserializationError(
            "VariablePaymentTerm.max_total_charge_amount required"
        )
    return out
