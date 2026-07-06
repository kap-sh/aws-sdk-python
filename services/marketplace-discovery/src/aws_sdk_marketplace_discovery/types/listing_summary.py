"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ListingSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.catalog
    import aws_sdk_marketplace_discovery.types.category_list
    import aws_sdk_marketplace_discovery.types.fulfillment_option_summary_list
    import aws_sdk_marketplace_discovery.types.listing_badge_list
    import aws_sdk_marketplace_discovery.types.listing_id
    import aws_sdk_marketplace_discovery.types.listing_summary_associated_entity_list
    import aws_sdk_marketplace_discovery.types.non_empty_string
    import aws_sdk_marketplace_discovery.types.pricing_model_list
    import aws_sdk_marketplace_discovery.types.pricing_unit_list
    import aws_sdk_marketplace_discovery.types.review_summary
    import aws_sdk_marketplace_discovery.types.seller_information
    import aws_sdk_marketplace_discovery.types.url


class ListingSummary(TypedDict, closed=True):
    listing_id: "aws_sdk_marketplace_discovery.types.listing_id.ListingId"
    """<p>The unique identifier of the listing.</p>"""
    listing_name: "aws_sdk_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>The human-readable display name of the listing.</p>"""
    publisher: (
        "aws_sdk_marketplace_discovery.types.seller_information.SellerInformation"
    )
    """<p>The entity who created and published the listing.</p>"""
    catalog: "aws_sdk_marketplace_discovery.types.catalog.Catalog"
    """<p>The name of the catalog that the listing belongs to.</p>"""
    short_description: (
        "aws_sdk_marketplace_discovery.types.non_empty_string.NonEmptyString"
    )
    """<p>A 1–3 sentence summary describing the key aspects of the listing.</p>"""
    logo_thumbnail_url: "aws_sdk_marketplace_discovery.types.url.URL"
    """<p>The URL of the logo thumbnail image for the listing.</p>"""
    categories: "aws_sdk_marketplace_discovery.types.category_list.CategoryList"
    """<p>The categories used to classify this listing into logical groups.</p>"""
    fulfillment_option_summaries: "aws_sdk_marketplace_discovery.types.fulfillment_option_summary_list.FulfillmentOptionSummaryList"
    """<p>A summary of fulfillment options available for the listing.</p>"""
    badges: "aws_sdk_marketplace_discovery.types.listing_badge_list.ListingBadgeList"
    """<p>Badges indicating special attributes of the listing.</p>"""
    review_summary: "aws_sdk_marketplace_discovery.types.review_summary.ReviewSummary"
    """<p>A summary of customer reviews for the listing.</p>"""
    pricing_models: (
        "aws_sdk_marketplace_discovery.types.pricing_model_list.PricingModelList"
    )
    """<p>The pricing models for offers associated with this listing.</p>"""
    pricing_units: (
        "aws_sdk_marketplace_discovery.types.pricing_unit_list.PricingUnitList"
    )
    """<p>The pricing units that define the billing dimensions for offers associated with this listing.</p>"""
    associated_entities: "aws_sdk_marketplace_discovery.types.listing_summary_associated_entity_list.ListingSummaryAssociatedEntityList"
    """<p>The products associated with this listing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListingSummary) -> dict:
    out: dict = {}
    out["listingId"] = value["listing_id"]
    out["listingName"] = value["listing_name"]
    import aws_sdk_marketplace_discovery.types.seller_information

    out["publisher"] = (
        aws_sdk_marketplace_discovery.types.seller_information.serialize_json(
            value["publisher"]
        )
    )
    out["catalog"] = value["catalog"]
    out["shortDescription"] = value["short_description"]
    out["logoThumbnailUrl"] = value["logo_thumbnail_url"]
    import aws_sdk_marketplace_discovery.types.category_list

    out["categories"] = (
        aws_sdk_marketplace_discovery.types.category_list.serialize_json(
            value["categories"]
        )
    )
    import aws_sdk_marketplace_discovery.types.fulfillment_option_summary_list

    out["fulfillmentOptionSummaries"] = (
        aws_sdk_marketplace_discovery.types.fulfillment_option_summary_list.serialize_json(
            value["fulfillment_option_summaries"]
        )
    )
    import aws_sdk_marketplace_discovery.types.listing_badge_list

    out["badges"] = (
        aws_sdk_marketplace_discovery.types.listing_badge_list.serialize_json(
            value["badges"]
        )
    )
    import aws_sdk_marketplace_discovery.types.review_summary

    out["reviewSummary"] = (
        aws_sdk_marketplace_discovery.types.review_summary.serialize_json(
            value["review_summary"]
        )
    )
    import aws_sdk_marketplace_discovery.types.pricing_model_list

    out["pricingModels"] = (
        aws_sdk_marketplace_discovery.types.pricing_model_list.serialize_json(
            value["pricing_models"]
        )
    )
    import aws_sdk_marketplace_discovery.types.pricing_unit_list

    out["pricingUnits"] = (
        aws_sdk_marketplace_discovery.types.pricing_unit_list.serialize_json(
            value["pricing_units"]
        )
    )
    import aws_sdk_marketplace_discovery.types.listing_summary_associated_entity_list

    out["associatedEntities"] = (
        aws_sdk_marketplace_discovery.types.listing_summary_associated_entity_list.serialize_json(
            value["associated_entities"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListingSummary:
    out: ListingSummary = {}  # type: ignore[typeddict-item]
    if "listingId" in data:
        out["listing_id"] = data["listingId"]
    else:
        raise DeserializationError("ListingSummary.listing_id required")
    if "listingName" in data:
        out["listing_name"] = data["listingName"]
    else:
        raise DeserializationError("ListingSummary.listing_name required")
    if "publisher" in data:
        import aws_sdk_marketplace_discovery.types.seller_information

        out["publisher"] = (
            aws_sdk_marketplace_discovery.types.seller_information.deserialize_json(
                data["publisher"]
            )
        )
    else:
        raise DeserializationError("ListingSummary.publisher required")
    if "catalog" in data:
        out["catalog"] = data["catalog"]
    else:
        raise DeserializationError("ListingSummary.catalog required")
    if "shortDescription" in data:
        out["short_description"] = data["shortDescription"]
    else:
        raise DeserializationError("ListingSummary.short_description required")
    if "logoThumbnailUrl" in data:
        out["logo_thumbnail_url"] = data["logoThumbnailUrl"]
    else:
        raise DeserializationError("ListingSummary.logo_thumbnail_url required")
    if "categories" in data:
        import aws_sdk_marketplace_discovery.types.category_list

        out["categories"] = (
            aws_sdk_marketplace_discovery.types.category_list.deserialize_json(
                data["categories"]
            )
        )
    else:
        raise DeserializationError("ListingSummary.categories required")
    if "fulfillmentOptionSummaries" in data:
        import aws_sdk_marketplace_discovery.types.fulfillment_option_summary_list

        out["fulfillment_option_summaries"] = (
            aws_sdk_marketplace_discovery.types.fulfillment_option_summary_list.deserialize_json(
                data["fulfillmentOptionSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListingSummary.fulfillment_option_summaries required"
        )
    if "badges" in data:
        import aws_sdk_marketplace_discovery.types.listing_badge_list

        out["badges"] = (
            aws_sdk_marketplace_discovery.types.listing_badge_list.deserialize_json(
                data["badges"]
            )
        )
    else:
        raise DeserializationError("ListingSummary.badges required")
    if "reviewSummary" in data:
        import aws_sdk_marketplace_discovery.types.review_summary

        out["review_summary"] = (
            aws_sdk_marketplace_discovery.types.review_summary.deserialize_json(
                data["reviewSummary"]
            )
        )
    else:
        raise DeserializationError("ListingSummary.review_summary required")
    if "pricingModels" in data:
        import aws_sdk_marketplace_discovery.types.pricing_model_list

        out["pricing_models"] = (
            aws_sdk_marketplace_discovery.types.pricing_model_list.deserialize_json(
                data["pricingModels"]
            )
        )
    else:
        raise DeserializationError("ListingSummary.pricing_models required")
    if "pricingUnits" in data:
        import aws_sdk_marketplace_discovery.types.pricing_unit_list

        out["pricing_units"] = (
            aws_sdk_marketplace_discovery.types.pricing_unit_list.deserialize_json(
                data["pricingUnits"]
            )
        )
    else:
        raise DeserializationError("ListingSummary.pricing_units required")
    if "associatedEntities" in data:
        import aws_sdk_marketplace_discovery.types.listing_summary_associated_entity_list

        out["associated_entities"] = (
            aws_sdk_marketplace_discovery.types.listing_summary_associated_entity_list.deserialize_json(
                data["associatedEntities"]
            )
        )
    else:
        raise DeserializationError("ListingSummary.associated_entities required")
    return out
