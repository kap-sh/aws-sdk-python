"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PricingUnit``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.non_empty_string
    import aws_sdk_marketplace_discovery.types.pricing_unit_type


class PricingUnit(TypedDict, closed=True):
    pricing_unit_type: (
        "aws_sdk_marketplace_discovery.types.pricing_unit_type.PricingUnitType"
    )
    """<p>The machine-readable type of the pricing unit.</p>"""
    display_name: "aws_sdk_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>The human-readable name of the pricing unit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PricingUnit) -> dict:
    out: dict = {}
    import aws_sdk_marketplace_discovery.types.pricing_unit_type

    out["pricingUnitType"] = (
        aws_sdk_marketplace_discovery.types.pricing_unit_type.serialize_json(
            value["pricing_unit_type"]
        )
    )
    out["displayName"] = value["display_name"]
    return out


def deserialize_json(data: dict) -> PricingUnit:
    out: PricingUnit = {}  # type: ignore[typeddict-item]
    if "pricingUnitType" in data:
        import aws_sdk_marketplace_discovery.types.pricing_unit_type

        out["pricing_unit_type"] = (
            aws_sdk_marketplace_discovery.types.pricing_unit_type.deserialize_json(
                data["pricingUnitType"]
            )
        )
    else:
        raise DeserializationError("PricingUnit.pricing_unit_type required")
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("PricingUnit.display_name required")
    return out
