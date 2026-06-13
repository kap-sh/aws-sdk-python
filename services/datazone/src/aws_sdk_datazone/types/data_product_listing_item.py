"""Generated from Smithy shape ``com.amazonaws.datazone#DataProductListingItem``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.created_at
    import aws_sdk_datazone.types.created_by
    import aws_sdk_datazone.types.data_product_id
    import aws_sdk_datazone.types.data_product_listing_item_additional_attributes
    import aws_sdk_datazone.types.data_product_name
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.detailed_glossary_terms
    import aws_sdk_datazone.types.listing_id
    import aws_sdk_datazone.types.listing_summary_items
    import aws_sdk_datazone.types.project_id
    import aws_sdk_datazone.types.revision
    import aws_sdk_datazone.types.updated_by


class DataProductListingItem(TypedDict):
    listing_id: NotRequired["aws_sdk_datazone.types.listing_id.ListingId"]
    """<p>The ID of the listing.</p>"""
    listing_revision: NotRequired["aws_sdk_datazone.types.revision.Revision"]
    """<p>The revision of the listing.</p>"""
    name: NotRequired["aws_sdk_datazone.types.data_product_name.DataProductName"]
    """<p>The name of the asset of the data product. </p>"""
    entity_id: NotRequired["aws_sdk_datazone.types.data_product_id.DataProductId"]
    """<p>The entity ID of the asset of the asset of the data product. </p>"""
    entity_revision: NotRequired["aws_sdk_datazone.types.revision.Revision"]
    """<p>The revision of the asset of the asset of the data product. </p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The description of the asset of the asset of the data product. </p>"""
    created_at: NotRequired["aws_sdk_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp at which the asset of the data product listing was created. </p>"""
    listing_created_by: NotRequired["aws_sdk_datazone.types.created_by.CreatedBy"]
    """<p>The timestamp at which the listing was created.</p>"""
    listing_updated_by: NotRequired["aws_sdk_datazone.types.updated_by.UpdatedBy"]
    """<p>The user who updated the listing.</p>"""
    glossary_terms: NotRequired[
        "aws_sdk_datazone.types.detailed_glossary_terms.DetailedGlossaryTerms"
    ]
    """<p>The glossary terms of the asset of the asset of the data product. </p>"""
    owning_project_id: NotRequired["aws_sdk_datazone.types.project_id.ProjectId"]
    """<p>The ID of the owning project of the asset of the data product. </p>"""
    additional_attributes: NotRequired[
        "aws_sdk_datazone.types.data_product_listing_item_additional_attributes.DataProductListingItemAdditionalAttributes"
    ]
    """<p>The additional attributes of the asset of the data product.</p>"""
    items: NotRequired[
        "aws_sdk_datazone.types.listing_summary_items.ListingSummaryItems"
    ]
    """<p>The data of the asset of the data product. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataProductListingItem) -> dict:
    out: dict = {}
    if "listing_id" in value:
        out["listingId"] = value["listing_id"]
    if "listing_revision" in value:
        out["listingRevision"] = value["listing_revision"]
    if "name" in value:
        out["name"] = value["name"]
    if "entity_id" in value:
        out["entityId"] = value["entity_id"]
    if "entity_revision" in value:
        out["entityRevision"] = value["entity_revision"]
    if "description" in value:
        out["description"] = value["description"]
    if "created_at" in value:
        import aws_sdk_datazone.types.created_at

        out["createdAt"] = aws_sdk_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "listing_created_by" in value:
        out["listingCreatedBy"] = value["listing_created_by"]
    if "listing_updated_by" in value:
        out["listingUpdatedBy"] = value["listing_updated_by"]
    if "glossary_terms" in value:
        import aws_sdk_datazone.types.detailed_glossary_terms

        out["glossaryTerms"] = (
            aws_sdk_datazone.types.detailed_glossary_terms.serialize_json(
                value["glossary_terms"]
            )
        )
    if "owning_project_id" in value:
        out["owningProjectId"] = value["owning_project_id"]
    if "additional_attributes" in value:
        import aws_sdk_datazone.types.data_product_listing_item_additional_attributes

        out["additionalAttributes"] = (
            aws_sdk_datazone.types.data_product_listing_item_additional_attributes.serialize_json(
                value["additional_attributes"]
            )
        )
    if "items" in value:
        import aws_sdk_datazone.types.listing_summary_items

        out["items"] = aws_sdk_datazone.types.listing_summary_items.serialize_json(
            value["items"]
        )
    return out


def deserialize_json(data: dict) -> DataProductListingItem:
    out: DataProductListingItem = {}  # type: ignore[typeddict-item]
    if "listingId" in data:
        out["listing_id"] = data["listingId"]
    if "listingRevision" in data:
        out["listing_revision"] = data["listingRevision"]
    if "name" in data:
        out["name"] = data["name"]
    if "entityId" in data:
        out["entity_id"] = data["entityId"]
    if "entityRevision" in data:
        out["entity_revision"] = data["entityRevision"]
    if "description" in data:
        out["description"] = data["description"]
    if "createdAt" in data:
        import aws_sdk_datazone.types.created_at

        out["created_at"] = aws_sdk_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if "listingCreatedBy" in data:
        out["listing_created_by"] = data["listingCreatedBy"]
    if "listingUpdatedBy" in data:
        out["listing_updated_by"] = data["listingUpdatedBy"]
    if "glossaryTerms" in data:
        import aws_sdk_datazone.types.detailed_glossary_terms

        out["glossary_terms"] = (
            aws_sdk_datazone.types.detailed_glossary_terms.deserialize_json(
                data["glossaryTerms"]
            )
        )
    if "owningProjectId" in data:
        out["owning_project_id"] = data["owningProjectId"]
    if "additionalAttributes" in data:
        import aws_sdk_datazone.types.data_product_listing_item_additional_attributes

        out["additional_attributes"] = (
            aws_sdk_datazone.types.data_product_listing_item_additional_attributes.deserialize_json(
                data["additionalAttributes"]
            )
        )
    if "items" in data:
        import aws_sdk_datazone.types.listing_summary_items

        out["items"] = aws_sdk_datazone.types.listing_summary_items.deserialize_json(
            data["items"]
        )
    return out
