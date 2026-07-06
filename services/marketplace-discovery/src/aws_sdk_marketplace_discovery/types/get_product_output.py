"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#GetProductOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.catalog
    import aws_sdk_marketplace_discovery.types.category_list
    import aws_sdk_marketplace_discovery.types.deployed_on_aws_status
    import aws_sdk_marketplace_discovery.types.fulfillment_option_summary_list
    import aws_sdk_marketplace_discovery.types.highlight_list
    import aws_sdk_marketplace_discovery.types.non_empty_string
    import aws_sdk_marketplace_discovery.types.product_id
    import aws_sdk_marketplace_discovery.types.promotional_media_list
    import aws_sdk_marketplace_discovery.types.resource_list
    import aws_sdk_marketplace_discovery.types.seller_engagement_list
    import aws_sdk_marketplace_discovery.types.seller_information
    import aws_sdk_marketplace_discovery.types.url


class GetProductOutput(TypedDict, closed=True):
    product_id: "aws_sdk_marketplace_discovery.types.product_id.ProductId"
    """<p>The unique identifier of the product.</p>"""
    catalog: "aws_sdk_marketplace_discovery.types.catalog.Catalog"
    """<p>The name of the catalog that the product belongs to.</p>"""
    product_name: "aws_sdk_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>The human-readable display name of the product.</p>"""
    deployed_on_aws: (
        "aws_sdk_marketplace_discovery.types.deployed_on_aws_status.DeployedOnAwsStatus"
    )
    """<p>Indicates whether the product is deployed on AWS infrastructure.</p>"""
    short_description: (
        "aws_sdk_marketplace_discovery.types.non_empty_string.NonEmptyString"
    )
    """<p>A 1–3 sentence summary describing the key aspects of the product.</p>"""
    long_description: (
        "aws_sdk_marketplace_discovery.types.non_empty_string.NonEmptyString"
    )
    """<p>A detailed description of what the product does, in paragraph format.</p>"""
    manufacturer: (
        "aws_sdk_marketplace_discovery.types.seller_information.SellerInformation"
    )
    """<p>The entity who manufactured the product.</p>"""
    logo_thumbnail_url: "aws_sdk_marketplace_discovery.types.url.URL"
    """<p>The URL of the logo thumbnail image for the product.</p>"""
    fulfillment_option_summaries: "aws_sdk_marketplace_discovery.types.fulfillment_option_summary_list.FulfillmentOptionSummaryList"
    """<p>A summary of fulfillment options available for deploying or accessing the product, such as AMI, SaaS, or Container.</p>"""
    categories: "aws_sdk_marketplace_discovery.types.category_list.CategoryList"
    """<p>The categories used to classify this product into logical groups.</p>"""
    highlights: "aws_sdk_marketplace_discovery.types.highlight_list.HighlightList"
    """<p>A list of key features that the product offers to customers.</p>"""
    promotional_media: "aws_sdk_marketplace_discovery.types.promotional_media_list.PromotionalMediaList"
    """<p>Embedded promotional media provided by the creator of the product, such as images and videos.</p>"""
    resources: "aws_sdk_marketplace_discovery.types.resource_list.ResourceList"
    """<p>Resources that provide further information about using the product or requesting support, such as documentation links, support contacts, and usage instructions.</p>"""
    seller_engagements: "aws_sdk_marketplace_discovery.types.seller_engagement_list.SellerEngagementList"
    """<p>Engagement options available to potential buyers, such as requesting a private offer or requesting a demo.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProductOutput) -> dict:
    out: dict = {}
    out["productId"] = value["product_id"]
    out["catalog"] = value["catalog"]
    out["productName"] = value["product_name"]
    import aws_sdk_marketplace_discovery.types.deployed_on_aws_status

    out["deployedOnAws"] = (
        aws_sdk_marketplace_discovery.types.deployed_on_aws_status.serialize_json(
            value["deployed_on_aws"]
        )
    )
    out["shortDescription"] = value["short_description"]
    out["longDescription"] = value["long_description"]
    import aws_sdk_marketplace_discovery.types.seller_information

    out["manufacturer"] = (
        aws_sdk_marketplace_discovery.types.seller_information.serialize_json(
            value["manufacturer"]
        )
    )
    out["logoThumbnailUrl"] = value["logo_thumbnail_url"]
    import aws_sdk_marketplace_discovery.types.fulfillment_option_summary_list

    out["fulfillmentOptionSummaries"] = (
        aws_sdk_marketplace_discovery.types.fulfillment_option_summary_list.serialize_json(
            value["fulfillment_option_summaries"]
        )
    )
    import aws_sdk_marketplace_discovery.types.category_list

    out["categories"] = (
        aws_sdk_marketplace_discovery.types.category_list.serialize_json(
            value["categories"]
        )
    )
    import aws_sdk_marketplace_discovery.types.highlight_list

    out["highlights"] = (
        aws_sdk_marketplace_discovery.types.highlight_list.serialize_json(
            value["highlights"]
        )
    )
    import aws_sdk_marketplace_discovery.types.promotional_media_list

    out["promotionalMedia"] = (
        aws_sdk_marketplace_discovery.types.promotional_media_list.serialize_json(
            value["promotional_media"]
        )
    )
    import aws_sdk_marketplace_discovery.types.resource_list

    out["resources"] = aws_sdk_marketplace_discovery.types.resource_list.serialize_json(
        value["resources"]
    )
    import aws_sdk_marketplace_discovery.types.seller_engagement_list

    out["sellerEngagements"] = (
        aws_sdk_marketplace_discovery.types.seller_engagement_list.serialize_json(
            value["seller_engagements"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetProductOutput:
    out: GetProductOutput = {}  # type: ignore[typeddict-item]
    if "productId" in data:
        out["product_id"] = data["productId"]
    else:
        raise DeserializationError("GetProductOutput.product_id required")
    if "catalog" in data:
        out["catalog"] = data["catalog"]
    else:
        raise DeserializationError("GetProductOutput.catalog required")
    if "productName" in data:
        out["product_name"] = data["productName"]
    else:
        raise DeserializationError("GetProductOutput.product_name required")
    if "deployedOnAws" in data:
        import aws_sdk_marketplace_discovery.types.deployed_on_aws_status

        out["deployed_on_aws"] = (
            aws_sdk_marketplace_discovery.types.deployed_on_aws_status.deserialize_json(
                data["deployedOnAws"]
            )
        )
    else:
        raise DeserializationError("GetProductOutput.deployed_on_aws required")
    if "shortDescription" in data:
        out["short_description"] = data["shortDescription"]
    else:
        raise DeserializationError("GetProductOutput.short_description required")
    if "longDescription" in data:
        out["long_description"] = data["longDescription"]
    else:
        raise DeserializationError("GetProductOutput.long_description required")
    if "manufacturer" in data:
        import aws_sdk_marketplace_discovery.types.seller_information

        out["manufacturer"] = (
            aws_sdk_marketplace_discovery.types.seller_information.deserialize_json(
                data["manufacturer"]
            )
        )
    else:
        raise DeserializationError("GetProductOutput.manufacturer required")
    if "logoThumbnailUrl" in data:
        out["logo_thumbnail_url"] = data["logoThumbnailUrl"]
    else:
        raise DeserializationError("GetProductOutput.logo_thumbnail_url required")
    if "fulfillmentOptionSummaries" in data:
        import aws_sdk_marketplace_discovery.types.fulfillment_option_summary_list

        out["fulfillment_option_summaries"] = (
            aws_sdk_marketplace_discovery.types.fulfillment_option_summary_list.deserialize_json(
                data["fulfillmentOptionSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "GetProductOutput.fulfillment_option_summaries required"
        )
    if "categories" in data:
        import aws_sdk_marketplace_discovery.types.category_list

        out["categories"] = (
            aws_sdk_marketplace_discovery.types.category_list.deserialize_json(
                data["categories"]
            )
        )
    else:
        raise DeserializationError("GetProductOutput.categories required")
    if "highlights" in data:
        import aws_sdk_marketplace_discovery.types.highlight_list

        out["highlights"] = (
            aws_sdk_marketplace_discovery.types.highlight_list.deserialize_json(
                data["highlights"]
            )
        )
    else:
        raise DeserializationError("GetProductOutput.highlights required")
    if "promotionalMedia" in data:
        import aws_sdk_marketplace_discovery.types.promotional_media_list

        out["promotional_media"] = (
            aws_sdk_marketplace_discovery.types.promotional_media_list.deserialize_json(
                data["promotionalMedia"]
            )
        )
    else:
        raise DeserializationError("GetProductOutput.promotional_media required")
    if "resources" in data:
        import aws_sdk_marketplace_discovery.types.resource_list

        out["resources"] = (
            aws_sdk_marketplace_discovery.types.resource_list.deserialize_json(
                data["resources"]
            )
        )
    else:
        raise DeserializationError("GetProductOutput.resources required")
    if "sellerEngagements" in data:
        import aws_sdk_marketplace_discovery.types.seller_engagement_list

        out["seller_engagements"] = (
            aws_sdk_marketplace_discovery.types.seller_engagement_list.deserialize_json(
                data["sellerEngagements"]
            )
        )
    else:
        raise DeserializationError("GetProductOutput.seller_engagements required")
    return out
