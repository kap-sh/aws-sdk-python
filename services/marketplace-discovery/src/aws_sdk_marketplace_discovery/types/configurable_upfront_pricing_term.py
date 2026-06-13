"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ConfigurableUpfrontPricingTerm``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.configurable_upfront_rate_card_list
    import aws_sdk_marketplace_discovery.types.currency_code
    import aws_sdk_marketplace_discovery.types.term_id
    import aws_sdk_marketplace_discovery.types.term_type


class ConfigurableUpfrontPricingTerm(TypedDict):
    id: "aws_sdk_marketplace_discovery.types.term_id.TermId"
    """<p>The unique identifier of the term.</p>"""
    type: "aws_sdk_marketplace_discovery.types.term_type.TermType"
    """<p>The category of the term.</p>"""
    currency_code: "aws_sdk_marketplace_discovery.types.currency_code.CurrencyCode"
    """<p>Defines the currency for the prices in this term.</p>"""
    rate_cards: NotRequired[
        "aws_sdk_marketplace_discovery.types.configurable_upfront_rate_card_list.ConfigurableUpfrontRateCardList"
    ]
    """<p>The rate cards available for selection, each with a selector, constraints, and per-unit rates.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurableUpfrontPricingTerm) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import aws_sdk_marketplace_discovery.types.term_type

    out["type"] = aws_sdk_marketplace_discovery.types.term_type.serialize_json(
        value["type"]
    )
    out["currencyCode"] = value["currency_code"]
    if "rate_cards" in value:
        import aws_sdk_marketplace_discovery.types.configurable_upfront_rate_card_list

        out["rateCards"] = (
            aws_sdk_marketplace_discovery.types.configurable_upfront_rate_card_list.serialize_json(
                value["rate_cards"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConfigurableUpfrontPricingTerm:
    out: ConfigurableUpfrontPricingTerm = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ConfigurableUpfrontPricingTerm.id required")
    if "type" in data:
        import aws_sdk_marketplace_discovery.types.term_type

        out["type"] = aws_sdk_marketplace_discovery.types.term_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("ConfigurableUpfrontPricingTerm.type required")
    if "currencyCode" in data:
        out["currency_code"] = data["currencyCode"]
    else:
        raise DeserializationError(
            "ConfigurableUpfrontPricingTerm.currency_code required"
        )
    if "rateCards" in data:
        import aws_sdk_marketplace_discovery.types.configurable_upfront_rate_card_list

        out["rate_cards"] = (
            aws_sdk_marketplace_discovery.types.configurable_upfront_rate_card_list.deserialize_json(
                data["rateCards"]
            )
        )
    return out
