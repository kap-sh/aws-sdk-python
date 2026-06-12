"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ConfigurableUpfrontRateCardItem``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_marketplace_discovery.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.constraints
    import aws_sdk_marketplace_discovery.types.rate_card_list
    import aws_sdk_marketplace_discovery.types.selector

class ConfigurableUpfrontRateCardItem(TypedDict):
    selector: "aws_sdk_marketplace_discovery.types.selector.Selector"
    """<p>The selector criteria for this rate card, such as duration.</p>"""
    constraints: "aws_sdk_marketplace_discovery.types.constraints.Constraints"
    """<p>Constraints on how the buyer can configure this rate card, such as whether multiple dimensions can be selected.</p>"""
    rate_card: "aws_sdk_marketplace_discovery.types.rate_card_list.RateCardList"
    """<p>The per-unit rates for this configuration.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ConfigurableUpfrontRateCardItem) -> dict:
    out: dict = {}
    import aws_sdk_marketplace_discovery.types.selector
    out["selector"] = aws_sdk_marketplace_discovery.types.selector.serialize_json(value["selector"])
    import aws_sdk_marketplace_discovery.types.constraints
    out["constraints"] = aws_sdk_marketplace_discovery.types.constraints.serialize_json(value["constraints"])
    import aws_sdk_marketplace_discovery.types.rate_card_list
    out["rateCard"] = aws_sdk_marketplace_discovery.types.rate_card_list.serialize_json(value["rate_card"])
    return out


def deserialize_json(data: dict) -> ConfigurableUpfrontRateCardItem:
    out: ConfigurableUpfrontRateCardItem = {}  # type: ignore[typeddict-item]
    if "selector" in data:
        import aws_sdk_marketplace_discovery.types.selector
        out["selector"] = aws_sdk_marketplace_discovery.types.selector.deserialize_json(data["selector"])
    else:
        raise DeserializationError("ConfigurableUpfrontRateCardItem.selector required")
    if "constraints" in data:
        import aws_sdk_marketplace_discovery.types.constraints
        out["constraints"] = aws_sdk_marketplace_discovery.types.constraints.deserialize_json(data["constraints"])
    else:
        raise DeserializationError("ConfigurableUpfrontRateCardItem.constraints required")
    if "rateCard" in data:
        import aws_sdk_marketplace_discovery.types.rate_card_list
        out["rate_card"] = aws_sdk_marketplace_discovery.types.rate_card_list.deserialize_json(data["rateCard"])
    else:
        raise DeserializationError("ConfigurableUpfrontRateCardItem.rate_card required")
    return out