"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#UsageBasedPricingTerm``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.currency_code
    import aws_sdk_marketplace_discovery.types.term_id
    import aws_sdk_marketplace_discovery.types.term_type
    import aws_sdk_marketplace_discovery.types.usage_based_rate_card_list


class UsageBasedPricingTerm(TypedDict):
    id: "aws_sdk_marketplace_discovery.types.term_id.TermId"
    """<p>The unique identifier of the term.</p>"""
    type: "aws_sdk_marketplace_discovery.types.term_type.TermType"
    """<p>The category of the term.</p>"""
    currency_code: "aws_sdk_marketplace_discovery.types.currency_code.CurrencyCode"
    """<p>Defines the currency for the prices in this term.</p>"""
    rate_cards: "aws_sdk_marketplace_discovery.types.usage_based_rate_card_list.UsageBasedRateCardList"
    """<p>The rate cards containing per-unit rates for usage-based pricing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UsageBasedPricingTerm) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import aws_sdk_marketplace_discovery.types.term_type

    out["type"] = aws_sdk_marketplace_discovery.types.term_type.serialize_json(
        value["type"]
    )
    out["currencyCode"] = value["currency_code"]
    import aws_sdk_marketplace_discovery.types.usage_based_rate_card_list

    out["rateCards"] = (
        aws_sdk_marketplace_discovery.types.usage_based_rate_card_list.serialize_json(
            value["rate_cards"]
        )
    )
    return out


def deserialize_json(data: dict) -> UsageBasedPricingTerm:
    out: UsageBasedPricingTerm = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("UsageBasedPricingTerm.id required")
    if "type" in data:
        import aws_sdk_marketplace_discovery.types.term_type

        out["type"] = aws_sdk_marketplace_discovery.types.term_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("UsageBasedPricingTerm.type required")
    if "currencyCode" in data:
        out["currency_code"] = data["currencyCode"]
    else:
        raise DeserializationError("UsageBasedPricingTerm.currency_code required")
    if "rateCards" in data:
        import aws_sdk_marketplace_discovery.types.usage_based_rate_card_list

        out["rate_cards"] = (
            aws_sdk_marketplace_discovery.types.usage_based_rate_card_list.deserialize_json(
                data["rateCards"]
            )
        )
    else:
        raise DeserializationError("UsageBasedPricingTerm.rate_cards required")
    return out
