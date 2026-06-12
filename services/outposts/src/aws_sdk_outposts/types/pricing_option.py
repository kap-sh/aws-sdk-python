"""Generated from Smithy shape ``com.amazonaws.outposts#PricingOption``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_outposts.types.quote_pricing_type
    import aws_sdk_outposts.types.subscription_pricing_details


class PricingOption(TypedDict):
    pricing_type: NotRequired[
        "aws_sdk_outposts.types.quote_pricing_type.QuotePricingType"
    ]
    """<p>The type of pricing model.</p>"""
    subscription_pricing_details: NotRequired[
        "aws_sdk_outposts.types.subscription_pricing_details.SubscriptionPricingDetails"
    ]
    """<p>The subscription pricing details for this pricing option.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PricingOption) -> dict:
    out: dict = {}
    if "pricing_type" in value:
        import aws_sdk_outposts.types.quote_pricing_type

        out["PricingType"] = aws_sdk_outposts.types.quote_pricing_type.serialize_json(
            value["pricing_type"]
        )
    if "subscription_pricing_details" in value:
        import aws_sdk_outposts.types.subscription_pricing_details

        out["SubscriptionPricingDetails"] = (
            aws_sdk_outposts.types.subscription_pricing_details.serialize_json(
                value["subscription_pricing_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> PricingOption:
    out: PricingOption = {}  # type: ignore[typeddict-item]
    if "PricingType" in data:
        import aws_sdk_outposts.types.quote_pricing_type

        out["pricing_type"] = (
            aws_sdk_outposts.types.quote_pricing_type.deserialize_json(
                data["PricingType"]
            )
        )
    if "SubscriptionPricingDetails" in data:
        import aws_sdk_outposts.types.subscription_pricing_details

        out["subscription_pricing_details"] = (
            aws_sdk_outposts.types.subscription_pricing_details.deserialize_json(
                data["SubscriptionPricingDetails"]
            )
        )
    return out
