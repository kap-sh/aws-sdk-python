"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#UsageBasedRateCardItem``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.rate_card_list


class UsageBasedRateCardItem(TypedDict):
    rate_card: "aws_sdk_marketplace_discovery.types.rate_card_list.RateCardList"
    """<p>The per-unit rates for this usage-based rate card.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UsageBasedRateCardItem) -> dict:
    out: dict = {}
    import aws_sdk_marketplace_discovery.types.rate_card_list

    out["rateCard"] = aws_sdk_marketplace_discovery.types.rate_card_list.serialize_json(
        value["rate_card"]
    )
    return out


def deserialize_json(data: dict) -> UsageBasedRateCardItem:
    out: UsageBasedRateCardItem = {}  # type: ignore[typeddict-item]
    if "rateCard" in data:
        import aws_sdk_marketplace_discovery.types.rate_card_list

        out["rate_card"] = (
            aws_sdk_marketplace_discovery.types.rate_card_list.deserialize_json(
                data["rateCard"]
            )
        )
    else:
        raise DeserializationError("UsageBasedRateCardItem.rate_card required")
    return out
