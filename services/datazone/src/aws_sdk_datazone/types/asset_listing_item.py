"""Generated from Smithy shape ``com.amazonaws.datazone#AssetListingItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.asset_id
    import aws_sdk_datazone.types.asset_listing_item_additional_attributes
    import aws_sdk_datazone.types.asset_name
    import aws_sdk_datazone.types.created_at
    import aws_sdk_datazone.types.created_by
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.detailed_glossary_terms
    import aws_sdk_datazone.types.listing_id
    import aws_sdk_datazone.types.project_id
    import aws_sdk_datazone.types.revision
    import aws_sdk_datazone.types.type_name
    import aws_sdk_datazone.types.updated_by


class AssetListingItem(TypedDict):
    listing_id: NotRequired["aws_sdk_datazone.types.listing_id.ListingId"]
    """<p>The identifier of the listing (asset published in Amazon DataZone catalog).</p>"""
    listing_revision: NotRequired["aws_sdk_datazone.types.revision.Revision"]
    """<p>The revision of the listing (asset published in Amazon DataZone catalog).</p>"""
    name: NotRequired["aws_sdk_datazone.types.asset_name.AssetName"]
    """<p>The name of the inventory asset.</p>"""
    entity_id: NotRequired["aws_sdk_datazone.types.asset_id.AssetId"]
    """<p>The identifier of the inventory asset.</p>"""
    entity_revision: NotRequired["aws_sdk_datazone.types.revision.Revision"]
    """<p>The revision of the inventory asset.</p>"""
    entity_type: NotRequired["aws_sdk_datazone.types.type_name.TypeName"]
    """<p>The type of the inventory asset.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The description of an asset published in an Amazon DataZone catalog.</p>"""
    created_at: NotRequired["aws_sdk_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp of when an asset published in an Amazon DataZone catalog was created.</p>"""
    listing_created_by: NotRequired["aws_sdk_datazone.types.created_by.CreatedBy"]
    """<p>The Amazon DataZone user who created the listing.</p>"""
    listing_updated_by: NotRequired["aws_sdk_datazone.types.updated_by.UpdatedBy"]
    """<p>The Amazon DataZone user who updated the listing.</p>"""
    glossary_terms: NotRequired[
        "aws_sdk_datazone.types.detailed_glossary_terms.DetailedGlossaryTerms"
    ]
    """<p>Glossary terms attached to the inventory asset.</p>"""
    governed_glossary_terms: NotRequired[
        "aws_sdk_datazone.types.detailed_glossary_terms.DetailedGlossaryTerms"
    ]
    """<p>The restricted glossary terms associated with an asset.</p>"""
    owning_project_id: NotRequired["aws_sdk_datazone.types.project_id.ProjectId"]
    """<p>The identifier of the project that owns the inventory asset.</p>"""
    additional_attributes: NotRequired[
        "aws_sdk_datazone.types.asset_listing_item_additional_attributes.AssetListingItemAdditionalAttributes"
    ]
    """<p>The additional attributes of an asset published in an Amazon DataZone catalog.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetListingItem) -> dict:
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
    if "entity_type" in value:
        out["entityType"] = value["entity_type"]
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
    if "governed_glossary_terms" in value:
        import aws_sdk_datazone.types.detailed_glossary_terms

        out["governedGlossaryTerms"] = (
            aws_sdk_datazone.types.detailed_glossary_terms.serialize_json(
                value["governed_glossary_terms"]
            )
        )
    if "owning_project_id" in value:
        out["owningProjectId"] = value["owning_project_id"]
    if "additional_attributes" in value:
        import aws_sdk_datazone.types.asset_listing_item_additional_attributes

        out["additionalAttributes"] = (
            aws_sdk_datazone.types.asset_listing_item_additional_attributes.serialize_json(
                value["additional_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssetListingItem:
    out: AssetListingItem = {}  # type: ignore[typeddict-item]
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
    if "entityType" in data:
        out["entity_type"] = data["entityType"]
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
    if "governedGlossaryTerms" in data:
        import aws_sdk_datazone.types.detailed_glossary_terms

        out["governed_glossary_terms"] = (
            aws_sdk_datazone.types.detailed_glossary_terms.deserialize_json(
                data["governedGlossaryTerms"]
            )
        )
    if "owningProjectId" in data:
        out["owning_project_id"] = data["owningProjectId"]
    if "additionalAttributes" in data:
        import aws_sdk_datazone.types.asset_listing_item_additional_attributes

        out["additional_attributes"] = (
            aws_sdk_datazone.types.asset_listing_item_additional_attributes.deserialize_json(
                data["additionalAttributes"]
            )
        )
    return out
