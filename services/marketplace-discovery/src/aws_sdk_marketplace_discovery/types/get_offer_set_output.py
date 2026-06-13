"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#GetOfferSetOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_marketplace_discovery.types.catalog
    import aws_sdk_marketplace_discovery.types.non_empty_string
    import aws_sdk_marketplace_discovery.types.nullable_string
    import aws_sdk_marketplace_discovery.types.offer_set_associated_entity_list
    import aws_sdk_marketplace_discovery.types.offer_set_id
    import aws_sdk_marketplace_discovery.types.purchase_option_badge_list
    import aws_sdk_marketplace_discovery.types.seller_information


class GetOfferSetOutput(TypedDict):
    offer_set_id: "aws_sdk_marketplace_discovery.types.offer_set_id.OfferSetId"
    """<p>The unique identifier of the offer set.</p>"""
    catalog: "aws_sdk_marketplace_discovery.types.catalog.Catalog"
    """<p>The name of the catalog that the offer set belongs to.</p>"""
    offer_set_name: NotRequired[
        "aws_sdk_marketplace_discovery.types.non_empty_string.NonEmptyString"
    ]
    """<p>The display name of the offer set.</p>"""
    available_from_time: NotRequired["datetime.datetime"]
    """<p>The date and time when the offer set became available to the buyer.</p>"""
    expiration_time: NotRequired["datetime.datetime"]
    """<p>The date and time when the offer set expires and is no longer available for procurement.</p>"""
    buyer_notes: NotRequired[
        "aws_sdk_marketplace_discovery.types.nullable_string.NullableString"
    ]
    """<p>Detailed information about the offer set that helps buyers understand its purpose and contents.</p>"""
    seller_of_record: (
        "aws_sdk_marketplace_discovery.types.seller_information.SellerInformation"
    )
    """<p>The entity responsible for selling the products under this offer set.</p>"""
    badges: "aws_sdk_marketplace_discovery.types.purchase_option_badge_list.PurchaseOptionBadgeList"
    """<p>Badges indicating special attributes of the offer set, such as private pricing or future dated.</p>"""
    associated_entities: "aws_sdk_marketplace_discovery.types.offer_set_associated_entity_list.OfferSetAssociatedEntityList"
    """<p>The products and offers included in this offer set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOfferSetOutput) -> dict:
    out: dict = {}
    out["offerSetId"] = value["offer_set_id"]
    out["catalog"] = value["catalog"]
    if "offer_set_name" in value:
        out["offerSetName"] = value["offer_set_name"]
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
    if "buyer_notes" in value:
        out["buyerNotes"] = value["buyer_notes"]
    import aws_sdk_marketplace_discovery.types.seller_information

    out["sellerOfRecord"] = (
        aws_sdk_marketplace_discovery.types.seller_information.serialize_json(
            value["seller_of_record"]
        )
    )
    import aws_sdk_marketplace_discovery.types.purchase_option_badge_list

    out["badges"] = (
        aws_sdk_marketplace_discovery.types.purchase_option_badge_list.serialize_json(
            value["badges"]
        )
    )
    import aws_sdk_marketplace_discovery.types.offer_set_associated_entity_list

    out["associatedEntities"] = (
        aws_sdk_marketplace_discovery.types.offer_set_associated_entity_list.serialize_json(
            value["associated_entities"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetOfferSetOutput:
    out: GetOfferSetOutput = {}  # type: ignore[typeddict-item]
    if "offerSetId" in data:
        out["offer_set_id"] = data["offerSetId"]
    else:
        raise DeserializationError("GetOfferSetOutput.offer_set_id required")
    if "catalog" in data:
        out["catalog"] = data["catalog"]
    else:
        raise DeserializationError("GetOfferSetOutput.catalog required")
    if "offerSetName" in data:
        out["offer_set_name"] = data["offerSetName"]
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
    if "buyerNotes" in data:
        out["buyer_notes"] = data["buyerNotes"]
    if "sellerOfRecord" in data:
        import aws_sdk_marketplace_discovery.types.seller_information

        out["seller_of_record"] = (
            aws_sdk_marketplace_discovery.types.seller_information.deserialize_json(
                data["sellerOfRecord"]
            )
        )
    else:
        raise DeserializationError("GetOfferSetOutput.seller_of_record required")
    if "badges" in data:
        import aws_sdk_marketplace_discovery.types.purchase_option_badge_list

        out["badges"] = (
            aws_sdk_marketplace_discovery.types.purchase_option_badge_list.deserialize_json(
                data["badges"]
            )
        )
    else:
        raise DeserializationError("GetOfferSetOutput.badges required")
    if "associatedEntities" in data:
        import aws_sdk_marketplace_discovery.types.offer_set_associated_entity_list

        out["associated_entities"] = (
            aws_sdk_marketplace_discovery.types.offer_set_associated_entity_list.deserialize_json(
                data["associatedEntities"]
            )
        )
    else:
        raise DeserializationError("GetOfferSetOutput.associated_entities required")
    return out
