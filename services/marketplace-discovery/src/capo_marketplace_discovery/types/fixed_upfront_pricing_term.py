"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#FixedUpfrontPricingTerm``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.bounded_string
    import capo_marketplace_discovery.types.currency_code
    import capo_marketplace_discovery.types.grant_list
    import capo_marketplace_discovery.types.term_id
    import capo_marketplace_discovery.types.term_type


class FixedUpfrontPricingTerm(TypedDict, closed=True):
    id: "capo_marketplace_discovery.types.term_id.TermId"
    """<p>The unique identifier of the term.</p>"""
    type: "capo_marketplace_discovery.types.term_type.TermType"
    """<p>The category of the term.</p>"""
    currency_code: "capo_marketplace_discovery.types.currency_code.CurrencyCode"
    """<p>Defines the currency for the prices in this term.</p>"""
    duration: NotRequired[
        "capo_marketplace_discovery.types.bounded_string.BoundedString"
    ]
    """<p>The duration of the fixed pricing term, in ISO 8601 format.</p>"""
    price: "capo_marketplace_discovery.types.bounded_string.BoundedString"
    """<p>The price charged upfront for this term.</p>"""
    grants: "capo_marketplace_discovery.types.grant_list.GrantList"
    """<p>The entitlements granted to the buyer as part of this term.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FixedUpfrontPricingTerm) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import capo_marketplace_discovery.types.term_type

    out["type"] = capo_marketplace_discovery.types.term_type.serialize_json(
        value["type"]
    )
    out["currencyCode"] = value["currency_code"]
    if "duration" in value:
        out["duration"] = value["duration"]
    out["price"] = value["price"]
    import capo_marketplace_discovery.types.grant_list

    out["grants"] = capo_marketplace_discovery.types.grant_list.serialize_json(
        value["grants"]
    )
    return out


def deserialize_json(data: dict) -> FixedUpfrontPricingTerm:
    out: FixedUpfrontPricingTerm = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("FixedUpfrontPricingTerm.id required")
    if "type" in data:
        import capo_marketplace_discovery.types.term_type

        out["type"] = capo_marketplace_discovery.types.term_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("FixedUpfrontPricingTerm.type required")
    if "currencyCode" in data:
        out["currency_code"] = data["currencyCode"]
    else:
        raise DeserializationError("FixedUpfrontPricingTerm.currency_code required")
    if "duration" in data:
        out["duration"] = data["duration"]
    if "price" in data:
        out["price"] = data["price"]
    else:
        raise DeserializationError("FixedUpfrontPricingTerm.price required")
    if "grants" in data:
        import capo_marketplace_discovery.types.grant_list

        out["grants"] = capo_marketplace_discovery.types.grant_list.deserialize_json(
            data["grants"]
        )
    else:
        raise DeserializationError("FixedUpfrontPricingTerm.grants required")
    return out
