"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ListingBadge``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.listing_badge_type
    import aws_sdk_marketplace_discovery.types.non_empty_string


class ListingBadge(TypedDict):
    display_name: "aws_sdk_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>The human-readable name of the badge.</p>"""
    badge_type: (
        "aws_sdk_marketplace_discovery.types.listing_badge_type.ListingBadgeType"
    )
    """<p>The machine-readable type of the badge.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListingBadge) -> dict:
    out: dict = {}
    out["displayName"] = value["display_name"]
    import aws_sdk_marketplace_discovery.types.listing_badge_type

    out["badgeType"] = (
        aws_sdk_marketplace_discovery.types.listing_badge_type.serialize_json(
            value["badge_type"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListingBadge:
    out: ListingBadge = {}  # type: ignore[typeddict-item]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("ListingBadge.display_name required")
    if "badgeType" in data:
        import aws_sdk_marketplace_discovery.types.listing_badge_type

        out["badge_type"] = (
            aws_sdk_marketplace_discovery.types.listing_badge_type.deserialize_json(
                data["badgeType"]
            )
        )
    else:
        raise DeserializationError("ListingBadge.badge_type required")
    return out
