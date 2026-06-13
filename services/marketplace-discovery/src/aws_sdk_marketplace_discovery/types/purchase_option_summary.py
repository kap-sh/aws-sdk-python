"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PurchaseOptionSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_marketplace_discovery.types.catalog
    import aws_sdk_marketplace_discovery.types.non_empty_string
    import aws_sdk_marketplace_discovery.types.purchase_option_associated_entity_list
    import aws_sdk_marketplace_discovery.types.purchase_option_badge_list
    import aws_sdk_marketplace_discovery.types.purchase_option_type
    import aws_sdk_marketplace_discovery.types.seller_information


class PurchaseOptionSummary(TypedDict):
    purchase_option_id: (
        "aws_sdk_marketplace_discovery.types.non_empty_string.NonEmptyString"
    )
    """<p>The unique identifier of the purchase option.</p>"""
    catalog: "aws_sdk_marketplace_discovery.types.catalog.Catalog"
    """<p>The name of the catalog that the purchase option belongs to.</p>"""
    purchase_option_type: (
        "aws_sdk_marketplace_discovery.types.purchase_option_type.PurchaseOptionType"
    )
    """<p>The type of purchase option. Values are <code>OFFER</code> for a single-product offer or <code>OFFERSET</code> for a bundled offer set.</p>"""
    purchase_option_name: NotRequired[
        "aws_sdk_marketplace_discovery.types.non_empty_string.NonEmptyString"
    ]
    """<p>The display name of the purchase option.</p>"""
    available_from_time: NotRequired["datetime.datetime"]
    """<p>The date and time when the purchase option became available to the buyer.</p>"""
    expiration_time: NotRequired["datetime.datetime"]
    """<p>The date and time when the purchase option expires and is no longer available for procurement.</p>"""
    seller_of_record: (
        "aws_sdk_marketplace_discovery.types.seller_information.SellerInformation"
    )
    """<p>The entity responsible for selling the product under this purchase option.</p>"""
    badges: NotRequired[
        "aws_sdk_marketplace_discovery.types.purchase_option_badge_list.PurchaseOptionBadgeList"
    ]
    """<p>Badges indicating special attributes of the purchase option, such as private pricing or future dated.</p>"""
    associated_entities: "aws_sdk_marketplace_discovery.types.purchase_option_associated_entity_list.PurchaseOptionAssociatedEntityList"
    """<p>The products, offers, and offer sets associated with this purchase option.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PurchaseOptionSummary) -> dict:
    out: dict = {}
    out["purchaseOptionId"] = value["purchase_option_id"]
    out["catalog"] = value["catalog"]
    import aws_sdk_marketplace_discovery.types.purchase_option_type

    out["purchaseOptionType"] = (
        aws_sdk_marketplace_discovery.types.purchase_option_type.serialize_json(
            value["purchase_option_type"]
        )
    )
    if "purchase_option_name" in value:
        out["purchaseOptionName"] = value["purchase_option_name"]
    if "available_from_time" in value:
        import aws_sdk_marketplace_discovery.types._prelude.timestamp

        out["availableFromTime"] = (
            aws_sdk_marketplace_discovery.types._prelude.timestamp.serialize_json(
                value["available_from_time"]
            )
        )
    if "expiration_time" in value:
        import aws_sdk_marketplace_discovery.types._prelude.timestamp

        out["expirationTime"] = (
            aws_sdk_marketplace_discovery.types._prelude.timestamp.serialize_json(
                value["expiration_time"]
            )
        )
    import aws_sdk_marketplace_discovery.types.seller_information

    out["sellerOfRecord"] = (
        aws_sdk_marketplace_discovery.types.seller_information.serialize_json(
            value["seller_of_record"]
        )
    )
    if "badges" in value:
        import aws_sdk_marketplace_discovery.types.purchase_option_badge_list

        out["badges"] = (
            aws_sdk_marketplace_discovery.types.purchase_option_badge_list.serialize_json(
                value["badges"]
            )
        )
    import aws_sdk_marketplace_discovery.types.purchase_option_associated_entity_list

    out["associatedEntities"] = (
        aws_sdk_marketplace_discovery.types.purchase_option_associated_entity_list.serialize_json(
            value["associated_entities"]
        )
    )
    return out


def deserialize_json(data: dict) -> PurchaseOptionSummary:
    out: PurchaseOptionSummary = {}  # type: ignore[typeddict-item]
    if "purchaseOptionId" in data:
        out["purchase_option_id"] = data["purchaseOptionId"]
    else:
        raise DeserializationError("PurchaseOptionSummary.purchase_option_id required")
    if "catalog" in data:
        out["catalog"] = data["catalog"]
    else:
        raise DeserializationError("PurchaseOptionSummary.catalog required")
    if "purchaseOptionType" in data:
        import aws_sdk_marketplace_discovery.types.purchase_option_type

        out["purchase_option_type"] = (
            aws_sdk_marketplace_discovery.types.purchase_option_type.deserialize_json(
                data["purchaseOptionType"]
            )
        )
    else:
        raise DeserializationError(
            "PurchaseOptionSummary.purchase_option_type required"
        )
    if "purchaseOptionName" in data:
        out["purchase_option_name"] = data["purchaseOptionName"]
    if "availableFromTime" in data:
        import aws_sdk_marketplace_discovery.types._prelude.timestamp

        out["available_from_time"] = (
            aws_sdk_marketplace_discovery.types._prelude.timestamp.deserialize_json(
                data["availableFromTime"]
            )
        )
    if "expirationTime" in data:
        import aws_sdk_marketplace_discovery.types._prelude.timestamp

        out["expiration_time"] = (
            aws_sdk_marketplace_discovery.types._prelude.timestamp.deserialize_json(
                data["expirationTime"]
            )
        )
    if "sellerOfRecord" in data:
        import aws_sdk_marketplace_discovery.types.seller_information

        out["seller_of_record"] = (
            aws_sdk_marketplace_discovery.types.seller_information.deserialize_json(
                data["sellerOfRecord"]
            )
        )
    else:
        raise DeserializationError("PurchaseOptionSummary.seller_of_record required")
    if "badges" in data:
        import aws_sdk_marketplace_discovery.types.purchase_option_badge_list

        out["badges"] = (
            aws_sdk_marketplace_discovery.types.purchase_option_badge_list.deserialize_json(
                data["badges"]
            )
        )
    if "associatedEntities" in data:
        import aws_sdk_marketplace_discovery.types.purchase_option_associated_entity_list

        out["associated_entities"] = (
            aws_sdk_marketplace_discovery.types.purchase_option_associated_entity_list.deserialize_json(
                data["associatedEntities"]
            )
        )
    else:
        raise DeserializationError("PurchaseOptionSummary.associated_entities required")
    return out
