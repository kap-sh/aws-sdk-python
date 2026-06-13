"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#SellerInformation``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.non_empty_string
    import aws_sdk_marketplace_discovery.types.seller_profile_id


class SellerInformation(TypedDict):
    seller_profile_id: (
        "aws_sdk_marketplace_discovery.types.seller_profile_id.SellerProfileId"
    )
    """<p>The unique identifier of the seller profile.</p>"""
    display_name: "aws_sdk_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>The human-readable name of the seller.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SellerInformation) -> dict:
    out: dict = {}
    out["sellerProfileId"] = value["seller_profile_id"]
    out["displayName"] = value["display_name"]
    return out


def deserialize_json(data: dict) -> SellerInformation:
    out: SellerInformation = {}  # type: ignore[typeddict-item]
    if "sellerProfileId" in data:
        out["seller_profile_id"] = data["sellerProfileId"]
    else:
        raise DeserializationError("SellerInformation.seller_profile_id required")
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("SellerInformation.display_name required")
    return out
