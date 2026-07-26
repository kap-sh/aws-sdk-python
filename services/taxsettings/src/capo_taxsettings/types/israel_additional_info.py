"""Generated from Smithy shape ``com.amazonaws.taxsettings#IsraelAdditionalInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_taxsettings.errors import DeserializationError

if TYPE_CHECKING:
    import capo_taxsettings.types.israel_customer_type
    import capo_taxsettings.types.israel_dealer_type


class IsraelAdditionalInfo(TypedDict, closed=True):
    dealer_type: "capo_taxsettings.types.israel_dealer_type.IsraelDealerType"
    """<p> Dealer type for your TRN in Israel. If you're not a local authorized dealer with an Israeli VAT ID, specify your tax identification number so that Amazon Web Services can send you a compliant tax invoice.</p>"""
    customer_type: "capo_taxsettings.types.israel_customer_type.IsraelCustomerType"
    """<p> Customer type for your TRN in Israel. The value can be <code>Business</code> or <code>Individual</code>. Use <code>Business</code>for entities such as not-for-profit and financial institutions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IsraelAdditionalInfo) -> dict:
    out: dict = {}
    import capo_taxsettings.types.israel_dealer_type

    out["dealerType"] = capo_taxsettings.types.israel_dealer_type.serialize_json(
        value["dealer_type"]
    )
    import capo_taxsettings.types.israel_customer_type

    out["customerType"] = capo_taxsettings.types.israel_customer_type.serialize_json(
        value["customer_type"]
    )
    return out


def deserialize_json(data: dict) -> IsraelAdditionalInfo:
    out: IsraelAdditionalInfo = {}  # type: ignore[typeddict-item]
    if "dealerType" in data:
        import capo_taxsettings.types.israel_dealer_type

        out["dealer_type"] = capo_taxsettings.types.israel_dealer_type.deserialize_json(
            data["dealerType"]
        )
    else:
        raise DeserializationError("IsraelAdditionalInfo.dealer_type required")
    if "customerType" in data:
        import capo_taxsettings.types.israel_customer_type

        out["customer_type"] = (
            capo_taxsettings.types.israel_customer_type.deserialize_json(
                data["customerType"]
            )
        )
    else:
        raise DeserializationError("IsraelAdditionalInfo.customer_type required")
    return out
