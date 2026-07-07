"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#GetOfferOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_marketplace_discovery.types.agreement_resource_id
    import aws_sdk_marketplace_discovery.types.catalog
    import aws_sdk_marketplace_discovery.types.nullable_string
    import aws_sdk_marketplace_discovery.types.offer_associated_entity_list
    import aws_sdk_marketplace_discovery.types.offer_id
    import aws_sdk_marketplace_discovery.types.pricing_model
    import aws_sdk_marketplace_discovery.types.purchase_option_badge_list
    import aws_sdk_marketplace_discovery.types.seller_information


class GetOfferOutput(TypedDict, closed=True):
    offer_id: "aws_sdk_marketplace_discovery.types.offer_id.OfferId"
    """<p>The unique identifier of the offer.</p>"""
    catalog: "aws_sdk_marketplace_discovery.types.catalog.Catalog"
    """<p>The name of the catalog that the offer belongs to.</p>"""
    offer_name: NotRequired[
        "aws_sdk_marketplace_discovery.types.nullable_string.NullableString"
    ]
    """<p>The display name of the offer. This is free-form text provided by the seller.</p>"""
    agreement_proposal_id: (
        "aws_sdk_marketplace_discovery.types.agreement_resource_id.AgreementResourceId"
    )
    """<p>An encoded string to be passed by the acceptor of the terms when creating an agreement.</p>"""
    expiration_time: NotRequired["datetime.datetime"]
    """<p>The date and time until when the offer can be procured. This value is null for offers that never expire.</p>"""
    available_from_time: NotRequired["datetime.datetime"]
    """<p>The date and time when the offer became available to the buyer.</p>"""
    seller_of_record: (
        "aws_sdk_marketplace_discovery.types.seller_information.SellerInformation"
    )
    """<p>The entity responsible for selling the product under this offer.</p>"""
    replacement_agreement_id: NotRequired[
        "aws_sdk_marketplace_discovery.types.agreement_resource_id.AgreementResourceId"
    ]
    """<p>The identifier of the existing agreement that this offer would replace. Enables agreement-based offer functionality.</p>"""
    pricing_model: "aws_sdk_marketplace_discovery.types.pricing_model.PricingModel"
    """<p>The pricing model that determines how buyers are charged, such as usage-based, contract, BYOL, or free.</p>"""
    badges: "aws_sdk_marketplace_discovery.types.purchase_option_badge_list.PurchaseOptionBadgeList"
    """<p>Badges indicating special attributes of the offer, such as private pricing, future dated, or replacement offer.</p>"""
    associated_entities: "aws_sdk_marketplace_discovery.types.offer_associated_entity_list.OfferAssociatedEntityList"
    """<p>The products and offer sets associated with this offer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOfferOutput) -> dict:
    out: dict = {}
    out["offerId"] = value["offer_id"]
    out["catalog"] = value["catalog"]
    if "offer_name" in value:
        out["offerName"] = value["offer_name"]
    out["agreementProposalId"] = value["agreement_proposal_id"]
    if "expiration_time" in value:
        import aws_sdk_marketplace_discovery.types._prelude.timestamp

        out["expirationTime"] = (
            aws_sdk_marketplace_discovery.types._prelude.timestamp.serialize_json(
                value["expiration_time"]
            )
        )
    if "available_from_time" in value:
        import aws_sdk_marketplace_discovery.types._prelude.timestamp

        out["availableFromTime"] = (
            aws_sdk_marketplace_discovery.types._prelude.timestamp.serialize_json(
                value["available_from_time"]
            )
        )
    import aws_sdk_marketplace_discovery.types.seller_information

    out["sellerOfRecord"] = (
        aws_sdk_marketplace_discovery.types.seller_information.serialize_json(
            value["seller_of_record"]
        )
    )
    if "replacement_agreement_id" in value:
        out["replacementAgreementId"] = value["replacement_agreement_id"]
    import aws_sdk_marketplace_discovery.types.pricing_model

    out["pricingModel"] = (
        aws_sdk_marketplace_discovery.types.pricing_model.serialize_json(
            value["pricing_model"]
        )
    )
    import aws_sdk_marketplace_discovery.types.purchase_option_badge_list

    out["badges"] = (
        aws_sdk_marketplace_discovery.types.purchase_option_badge_list.serialize_json(
            value["badges"]
        )
    )
    import aws_sdk_marketplace_discovery.types.offer_associated_entity_list

    out["associatedEntities"] = (
        aws_sdk_marketplace_discovery.types.offer_associated_entity_list.serialize_json(
            value["associated_entities"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetOfferOutput:
    out: GetOfferOutput = {}  # type: ignore[typeddict-item]
    if "offerId" in data:
        out["offer_id"] = data["offerId"]
    else:
        raise DeserializationError("GetOfferOutput.offer_id required")
    if "catalog" in data:
        out["catalog"] = data["catalog"]
    else:
        raise DeserializationError("GetOfferOutput.catalog required")
    if "offerName" in data:
        out["offer_name"] = data["offerName"]
    if "agreementProposalId" in data:
        out["agreement_proposal_id"] = data["agreementProposalId"]
    else:
        raise DeserializationError("GetOfferOutput.agreement_proposal_id required")
    if "expirationTime" in data:
        import aws_sdk_marketplace_discovery.types._prelude.timestamp

        out["expiration_time"] = (
            aws_sdk_marketplace_discovery.types._prelude.timestamp.deserialize_json(
                data["expirationTime"]
            )
        )
    if "availableFromTime" in data:
        import aws_sdk_marketplace_discovery.types._prelude.timestamp

        out["available_from_time"] = (
            aws_sdk_marketplace_discovery.types._prelude.timestamp.deserialize_json(
                data["availableFromTime"]
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
        raise DeserializationError("GetOfferOutput.seller_of_record required")
    if "replacementAgreementId" in data:
        out["replacement_agreement_id"] = data["replacementAgreementId"]
    if "pricingModel" in data:
        import aws_sdk_marketplace_discovery.types.pricing_model

        out["pricing_model"] = (
            aws_sdk_marketplace_discovery.types.pricing_model.deserialize_json(
                data["pricingModel"]
            )
        )
    else:
        raise DeserializationError("GetOfferOutput.pricing_model required")
    if "badges" in data:
        import aws_sdk_marketplace_discovery.types.purchase_option_badge_list

        out["badges"] = (
            aws_sdk_marketplace_discovery.types.purchase_option_badge_list.deserialize_json(
                data["badges"]
            )
        )
    else:
        raise DeserializationError("GetOfferOutput.badges required")
    if "associatedEntities" in data:
        import aws_sdk_marketplace_discovery.types.offer_associated_entity_list

        out["associated_entities"] = (
            aws_sdk_marketplace_discovery.types.offer_associated_entity_list.deserialize_json(
                data["associatedEntities"]
            )
        )
    else:
        raise DeserializationError("GetOfferOutput.associated_entities required")
    return out
