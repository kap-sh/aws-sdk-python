"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#MonetaryValue``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_partnercentral_benefits.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_benefits.types.currency_code


class MonetaryValue(TypedDict, closed=True):
    amount: "str"
    """<p>The numeric amount of the monetary value.</p>"""
    currency_code: "capo_partnercentral_benefits.types.currency_code.CurrencyCode"
    """<p>The ISO 4217 currency code (e.g., USD, EUR) for the monetary amount.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MonetaryValue) -> dict:
    out: dict = {}
    out["Amount"] = value["amount"]
    import capo_partnercentral_benefits.types.currency_code

    out["CurrencyCode"] = (
        capo_partnercentral_benefits.types.currency_code.serialize_aws_json_1_0(
            value["currency_code"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> MonetaryValue:
    out: MonetaryValue = {}  # type: ignore[typeddict-item]
    if "Amount" in data:
        out["amount"] = data["Amount"]
    else:
        raise DeserializationError("MonetaryValue.amount required")
    if "CurrencyCode" in data:
        import capo_partnercentral_benefits.types.currency_code

        out["currency_code"] = (
            capo_partnercentral_benefits.types.currency_code.deserialize_aws_json_1_0(
                data["CurrencyCode"]
            )
        )
    else:
        raise DeserializationError("MonetaryValue.currency_code required")
    return out
