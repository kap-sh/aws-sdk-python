"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PurchaseOptionBadge``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.non_empty_string
    import aws_sdk_marketplace_discovery.types.purchase_option_badge_type


class PurchaseOptionBadge(TypedDict, closed=True):
    display_name: "aws_sdk_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>The human-readable name of the badge.</p>"""
    badge_type: "aws_sdk_marketplace_discovery.types.purchase_option_badge_type.PurchaseOptionBadgeType"
    """<p>The machine-readable type of the badge.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PurchaseOptionBadge) -> dict:
    out: dict = {}
    out["displayName"] = value["display_name"]
    import aws_sdk_marketplace_discovery.types.purchase_option_badge_type

    out["badgeType"] = (
        aws_sdk_marketplace_discovery.types.purchase_option_badge_type.serialize_json(
            value["badge_type"]
        )
    )
    return out


def deserialize_json(data: dict) -> PurchaseOptionBadge:
    out: PurchaseOptionBadge = {}  # type: ignore[typeddict-item]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("PurchaseOptionBadge.display_name required")
    if "badgeType" in data:
        import aws_sdk_marketplace_discovery.types.purchase_option_badge_type

        out["badge_type"] = (
            aws_sdk_marketplace_discovery.types.purchase_option_badge_type.deserialize_json(
                data["badgeType"]
            )
        )
    else:
        raise DeserializationError("PurchaseOptionBadge.badge_type required")
    return out
