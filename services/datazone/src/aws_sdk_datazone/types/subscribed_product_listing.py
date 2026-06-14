"""Generated from Smithy shape ``com.amazonaws.datazone#SubscribedProductListing``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.asset_id
    import aws_sdk_datazone.types.asset_in_data_product_listing_items
    import aws_sdk_datazone.types.detailed_glossary_terms
    import aws_sdk_datazone.types.revision


class SubscribedProductListing(TypedDict):
    entity_id: NotRequired["aws_sdk_datazone.types.asset_id.AssetId"]
    """<p>The ID of the data product listing.</p>"""
    entity_revision: NotRequired["aws_sdk_datazone.types.revision.Revision"]
    """<p>The revision of the data product listing.</p>"""
    glossary_terms: NotRequired[
        "aws_sdk_datazone.types.detailed_glossary_terms.DetailedGlossaryTerms"
    ]
    """<p>The glossary terms of the data product listing.</p>"""
    name: NotRequired["str"]
    """<p>The name of the data product listing.</p>"""
    description: NotRequired["str"]
    """<p>The description of the data product listing.</p>"""
    asset_listings: NotRequired[
        "aws_sdk_datazone.types.asset_in_data_product_listing_items.AssetInDataProductListingItems"
    ]
    """<p>The data assets of the data product listing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubscribedProductListing) -> dict:
    out: dict = {}
    if "entity_id" in value:
        out["entityId"] = value["entity_id"]
    if "entity_revision" in value:
        out["entityRevision"] = value["entity_revision"]
    if "glossary_terms" in value:
        import aws_sdk_datazone.types.detailed_glossary_terms

        out["glossaryTerms"] = (
            aws_sdk_datazone.types.detailed_glossary_terms.serialize_json(
                value["glossary_terms"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "asset_listings" in value:
        import aws_sdk_datazone.types.asset_in_data_product_listing_items

        out["assetListings"] = (
            aws_sdk_datazone.types.asset_in_data_product_listing_items.serialize_json(
                value["asset_listings"]
            )
        )
    return out


def deserialize_json(data: dict) -> SubscribedProductListing:
    out: SubscribedProductListing = {}  # type: ignore[typeddict-item]
    if "entityId" in data:
        out["entity_id"] = data["entityId"]
    if "entityRevision" in data:
        out["entity_revision"] = data["entityRevision"]
    if "glossaryTerms" in data:
        import aws_sdk_datazone.types.detailed_glossary_terms

        out["glossary_terms"] = (
            aws_sdk_datazone.types.detailed_glossary_terms.deserialize_json(
                data["glossaryTerms"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "assetListings" in data:
        import aws_sdk_datazone.types.asset_in_data_product_listing_items

        out["asset_listings"] = (
            aws_sdk_datazone.types.asset_in_data_product_listing_items.deserialize_json(
                data["assetListings"]
            )
        )
    return out
