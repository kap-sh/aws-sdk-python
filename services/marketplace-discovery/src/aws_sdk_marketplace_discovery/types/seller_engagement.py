"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#SellerEngagement``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.non_empty_string
    import aws_sdk_marketplace_discovery.types.seller_engagement_content_type
    import aws_sdk_marketplace_discovery.types.seller_engagement_type


class SellerEngagement(TypedDict):
    engagement_type: "aws_sdk_marketplace_discovery.types.seller_engagement_type.SellerEngagementType"
    """<p>The type of engagement, such as <code>REQUEST_FOR_PRIVATE_OFFER</code> or <code>REQUEST_FOR_DEMO</code>.</p>"""
    content_type: "aws_sdk_marketplace_discovery.types.seller_engagement_content_type.SellerEngagementContentType"
    """<p>The format of the engagement value, such as a URL.</p>"""
    value: "aws_sdk_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>The engagement value, such as a URL to the engagement form.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SellerEngagement) -> dict:
    out: dict = {}
    import aws_sdk_marketplace_discovery.types.seller_engagement_type

    out["engagementType"] = (
        aws_sdk_marketplace_discovery.types.seller_engagement_type.serialize_json(
            value["engagement_type"]
        )
    )
    import aws_sdk_marketplace_discovery.types.seller_engagement_content_type

    out["contentType"] = (
        aws_sdk_marketplace_discovery.types.seller_engagement_content_type.serialize_json(
            value["content_type"]
        )
    )
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> SellerEngagement:
    out: SellerEngagement = {}  # type: ignore[typeddict-item]
    if "engagementType" in data:
        import aws_sdk_marketplace_discovery.types.seller_engagement_type

        out["engagement_type"] = (
            aws_sdk_marketplace_discovery.types.seller_engagement_type.deserialize_json(
                data["engagementType"]
            )
        )
    else:
        raise DeserializationError("SellerEngagement.engagement_type required")
    if "contentType" in data:
        import aws_sdk_marketplace_discovery.types.seller_engagement_content_type

        out["content_type"] = (
            aws_sdk_marketplace_discovery.types.seller_engagement_content_type.deserialize_json(
                data["contentType"]
            )
        )
    else:
        raise DeserializationError("SellerEngagement.content_type required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("SellerEngagement.value required")
    return out
