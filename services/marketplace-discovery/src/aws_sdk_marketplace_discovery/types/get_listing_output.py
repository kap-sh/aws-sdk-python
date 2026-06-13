"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#GetListingOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.catalog
    import aws_sdk_marketplace_discovery.types.category_list
    import aws_sdk_marketplace_discovery.types.fulfillment_option_summary_list
    import aws_sdk_marketplace_discovery.types.highlight_list
    import aws_sdk_marketplace_discovery.types.listing_associated_entity_list
    import aws_sdk_marketplace_discovery.types.listing_badge_list
    import aws_sdk_marketplace_discovery.types.listing_id
    import aws_sdk_marketplace_discovery.types.non_empty_string
    import aws_sdk_marketplace_discovery.types.nullable_string
    import aws_sdk_marketplace_discovery.types.pricing_model_list
    import aws_sdk_marketplace_discovery.types.pricing_unit_list
    import aws_sdk_marketplace_discovery.types.promotional_media_list
    import aws_sdk_marketplace_discovery.types.resource_list
    import aws_sdk_marketplace_discovery.types.review_summary
    import aws_sdk_marketplace_discovery.types.seller_engagement_list
    import aws_sdk_marketplace_discovery.types.seller_information
    import aws_sdk_marketplace_discovery.types.url
    import aws_sdk_marketplace_discovery.types.use_case_list


class GetListingOutput(TypedDict):
    associated_entities: "aws_sdk_marketplace_discovery.types.listing_associated_entity_list.ListingAssociatedEntityList"
    """<p>The products and offers associated with this listing. Each entity contains product and offer information.</p>"""
    badges: "aws_sdk_marketplace_discovery.types.listing_badge_list.ListingBadgeList"
    """<p>Badges indicating special attributes of the listing, such as free tier eligibility, free trial availability, or Quick Launch support.</p>"""
    catalog: "aws_sdk_marketplace_discovery.types.catalog.Catalog"
    """<p>The name of the catalog that the listing belongs to.</p>"""
    categories: "aws_sdk_marketplace_discovery.types.category_list.CategoryList"
    """<p>The categories used to classify this listing into logical groups.</p>"""
    fulfillment_option_summaries: "aws_sdk_marketplace_discovery.types.fulfillment_option_summary_list.FulfillmentOptionSummaryList"
    """<p>A summary of fulfillment options available for deploying or accessing the listing, such as AMI, SaaS, or Container.</p>"""
    highlights: "aws_sdk_marketplace_discovery.types.highlight_list.HighlightList"
    """<p>A list of key features that the listing offers to customers.</p>"""
    integration_guide: NotRequired[
        "aws_sdk_marketplace_discovery.types.nullable_string.NullableString"
    ]
    """<p>Optional guidance explaining how to use data in this listing. Primarily defines how to integrate with a multi-product listing.</p>"""
    listing_id: "aws_sdk_marketplace_discovery.types.listing_id.ListingId"
    """<p>The unique identifier of the listing.</p>"""
    listing_name: "aws_sdk_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>The human-readable display name of the listing.</p>"""
    logo_thumbnail_url: "aws_sdk_marketplace_discovery.types.url.URL"
    """<p>The URL of the logo thumbnail image for the listing.</p>"""
    long_description: (
        "aws_sdk_marketplace_discovery.types.non_empty_string.NonEmptyString"
    )
    """<p>A detailed description of what the listing offers, in paragraph format.</p>"""
    pricing_models: (
        "aws_sdk_marketplace_discovery.types.pricing_model_list.PricingModelList"
    )
    """<p>The pricing models for offers associated with this listing, such as usage-based, contract, BYOL, or free.</p>"""
    pricing_units: (
        "aws_sdk_marketplace_discovery.types.pricing_unit_list.PricingUnitList"
    )
    """<p>The pricing units that define the billing dimensions for offers associated with this listing, such as users, hosts, or data.</p>"""
    promotional_media: "aws_sdk_marketplace_discovery.types.promotional_media_list.PromotionalMediaList"
    """<p>Embedded promotional media provided by the creator of the product, such as images and videos.</p>"""
    publisher: (
        "aws_sdk_marketplace_discovery.types.seller_information.SellerInformation"
    )
    """<p>The entity who created and published the listing.</p>"""
    resources: "aws_sdk_marketplace_discovery.types.resource_list.ResourceList"
    """<p>Resources that provide further information about using the product or requesting support, such as documentation links, support contacts, and usage instructions.</p>"""
    review_summary: NotRequired[
        "aws_sdk_marketplace_discovery.types.review_summary.ReviewSummary"
    ]
    """<p>A summary of customer reviews available for the listing, including average rating and total review count by source.</p>"""
    seller_engagements: "aws_sdk_marketplace_discovery.types.seller_engagement_list.SellerEngagementList"
    """<p>Engagement options available to potential buyers, such as requesting a private offer or requesting a demo.</p>"""
    short_description: (
        "aws_sdk_marketplace_discovery.types.non_empty_string.NonEmptyString"
    )
    """<p>A 1–3 sentence summary describing the key aspects of the listing.</p>"""
    use_cases: "aws_sdk_marketplace_discovery.types.use_case_list.UseCaseList"
    """<p>Use cases associated with the listing, describing scenarios where the product can be applied.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetListingOutput) -> dict:
    out: dict = {}
    import aws_sdk_marketplace_discovery.types.listing_associated_entity_list

    out["associatedEntities"] = (
        aws_sdk_marketplace_discovery.types.listing_associated_entity_list.serialize_json(
            value["associated_entities"]
        )
    )
    import aws_sdk_marketplace_discovery.types.listing_badge_list

    out["badges"] = (
        aws_sdk_marketplace_discovery.types.listing_badge_list.serialize_json(
            value["badges"]
        )
    )
    out["catalog"] = value["catalog"]
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
    import aws_sdk_marketplace_discovery.types.highlight_list

    out["highlights"] = (
        aws_sdk_marketplace_discovery.types.highlight_list.serialize_json(
            value["highlights"]
        )
    )
    if "integration_guide" in value:
        out["integrationGuide"] = value["integration_guide"]
    out["listingId"] = value["listing_id"]
    out["listingName"] = value["listing_name"]
    out["logoThumbnailUrl"] = value["logo_thumbnail_url"]
    out["longDescription"] = value["long_description"]
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
    import aws_sdk_marketplace_discovery.types.promotional_media_list

    out["promotionalMedia"] = (
        aws_sdk_marketplace_discovery.types.promotional_media_list.serialize_json(
            value["promotional_media"]
        )
    )
    import aws_sdk_marketplace_discovery.types.seller_information

    out["publisher"] = (
        aws_sdk_marketplace_discovery.types.seller_information.serialize_json(
            value["publisher"]
        )
    )
    import aws_sdk_marketplace_discovery.types.resource_list

    out["resources"] = aws_sdk_marketplace_discovery.types.resource_list.serialize_json(
        value["resources"]
    )
    if "review_summary" in value:
        import aws_sdk_marketplace_discovery.types.review_summary

        out["reviewSummary"] = (
            aws_sdk_marketplace_discovery.types.review_summary.serialize_json(
                value["review_summary"]
            )
        )
    import aws_sdk_marketplace_discovery.types.seller_engagement_list

    out["sellerEngagements"] = (
        aws_sdk_marketplace_discovery.types.seller_engagement_list.serialize_json(
            value["seller_engagements"]
        )
    )
    out["shortDescription"] = value["short_description"]
    import aws_sdk_marketplace_discovery.types.use_case_list

    out["useCases"] = aws_sdk_marketplace_discovery.types.use_case_list.serialize_json(
        value["use_cases"]
    )
    return out


def deserialize_json(data: dict) -> GetListingOutput:
    out: GetListingOutput = {}  # type: ignore[typeddict-item]
    if "associatedEntities" in data:
        import aws_sdk_marketplace_discovery.types.listing_associated_entity_list

        out["associated_entities"] = (
            aws_sdk_marketplace_discovery.types.listing_associated_entity_list.deserialize_json(
                data["associatedEntities"]
            )
        )
    else:
        raise DeserializationError("GetListingOutput.associated_entities required")
    if "badges" in data:
        import aws_sdk_marketplace_discovery.types.listing_badge_list

        out["badges"] = (
            aws_sdk_marketplace_discovery.types.listing_badge_list.deserialize_json(
                data["badges"]
            )
        )
    else:
        raise DeserializationError("GetListingOutput.badges required")
    if "catalog" in data:
        out["catalog"] = data["catalog"]
    else:
        raise DeserializationError("GetListingOutput.catalog required")
    if "categories" in data:
        import aws_sdk_marketplace_discovery.types.category_list

        out["categories"] = (
            aws_sdk_marketplace_discovery.types.category_list.deserialize_json(
                data["categories"]
            )
        )
    else:
        raise DeserializationError("GetListingOutput.categories required")
    if "fulfillmentOptionSummaries" in data:
        import aws_sdk_marketplace_discovery.types.fulfillment_option_summary_list

        out["fulfillment_option_summaries"] = (
            aws_sdk_marketplace_discovery.types.fulfillment_option_summary_list.deserialize_json(
                data["fulfillmentOptionSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "GetListingOutput.fulfillment_option_summaries required"
        )
    if "highlights" in data:
        import aws_sdk_marketplace_discovery.types.highlight_list

        out["highlights"] = (
            aws_sdk_marketplace_discovery.types.highlight_list.deserialize_json(
                data["highlights"]
            )
        )
    else:
        raise DeserializationError("GetListingOutput.highlights required")
    if "integrationGuide" in data:
        out["integration_guide"] = data["integrationGuide"]
    if "listingId" in data:
        out["listing_id"] = data["listingId"]
    else:
        raise DeserializationError("GetListingOutput.listing_id required")
    if "listingName" in data:
        out["listing_name"] = data["listingName"]
    else:
        raise DeserializationError("GetListingOutput.listing_name required")
    if "logoThumbnailUrl" in data:
        out["logo_thumbnail_url"] = data["logoThumbnailUrl"]
    else:
        raise DeserializationError("GetListingOutput.logo_thumbnail_url required")
    if "longDescription" in data:
        out["long_description"] = data["longDescription"]
    else:
        raise DeserializationError("GetListingOutput.long_description required")
    if "pricingModels" in data:
        import aws_sdk_marketplace_discovery.types.pricing_model_list

        out["pricing_models"] = (
            aws_sdk_marketplace_discovery.types.pricing_model_list.deserialize_json(
                data["pricingModels"]
            )
        )
    else:
        raise DeserializationError("GetListingOutput.pricing_models required")
    if "pricingUnits" in data:
        import aws_sdk_marketplace_discovery.types.pricing_unit_list

        out["pricing_units"] = (
            aws_sdk_marketplace_discovery.types.pricing_unit_list.deserialize_json(
                data["pricingUnits"]
            )
        )
    else:
        raise DeserializationError("GetListingOutput.pricing_units required")
    if "promotionalMedia" in data:
        import aws_sdk_marketplace_discovery.types.promotional_media_list

        out["promotional_media"] = (
            aws_sdk_marketplace_discovery.types.promotional_media_list.deserialize_json(
                data["promotionalMedia"]
            )
        )
    else:
        raise DeserializationError("GetListingOutput.promotional_media required")
    if "publisher" in data:
        import aws_sdk_marketplace_discovery.types.seller_information

        out["publisher"] = (
            aws_sdk_marketplace_discovery.types.seller_information.deserialize_json(
                data["publisher"]
            )
        )
    else:
        raise DeserializationError("GetListingOutput.publisher required")
    if "resources" in data:
        import aws_sdk_marketplace_discovery.types.resource_list

        out["resources"] = (
            aws_sdk_marketplace_discovery.types.resource_list.deserialize_json(
                data["resources"]
            )
        )
    else:
        raise DeserializationError("GetListingOutput.resources required")
    if "reviewSummary" in data:
        import aws_sdk_marketplace_discovery.types.review_summary

        out["review_summary"] = (
            aws_sdk_marketplace_discovery.types.review_summary.deserialize_json(
                data["reviewSummary"]
            )
        )
    if "sellerEngagements" in data:
        import aws_sdk_marketplace_discovery.types.seller_engagement_list

        out["seller_engagements"] = (
            aws_sdk_marketplace_discovery.types.seller_engagement_list.deserialize_json(
                data["sellerEngagements"]
            )
        )
    else:
        raise DeserializationError("GetListingOutput.seller_engagements required")
    if "shortDescription" in data:
        out["short_description"] = data["shortDescription"]
    else:
        raise DeserializationError("GetListingOutput.short_description required")
    if "useCases" in data:
        import aws_sdk_marketplace_discovery.types.use_case_list

        out["use_cases"] = (
            aws_sdk_marketplace_discovery.types.use_case_list.deserialize_json(
                data["useCases"]
            )
        )
    else:
        raise DeserializationError("GetListingOutput.use_cases required")
    return out
