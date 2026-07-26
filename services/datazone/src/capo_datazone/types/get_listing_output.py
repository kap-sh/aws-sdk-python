"""Generated from Smithy shape ``com.amazonaws.datazone#GetListingOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.created_at
    import capo_datazone.types.created_by
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.listing_id
    import capo_datazone.types.listing_item
    import capo_datazone.types.listing_name
    import capo_datazone.types.listing_status
    import capo_datazone.types.revision
    import capo_datazone.types.updated_at
    import capo_datazone.types.updated_by


class GetListingOutput(TypedDict, closed=True):
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain.</p>"""
    id: "capo_datazone.types.listing_id.ListingId"
    """<p>The ID of the listing.</p>"""
    listing_revision: "capo_datazone.types.revision.Revision"
    """<p>The revision of a listing.</p>"""
    created_at: NotRequired["capo_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp of when the listing was created.</p>"""
    updated_at: NotRequired["capo_datazone.types.updated_at.UpdatedAt"]
    """<p>The timestamp of when the listing was updated.</p>"""
    created_by: NotRequired["capo_datazone.types.created_by.CreatedBy"]
    """<p>The Amazon DataZone user who created the listing.</p>"""
    updated_by: NotRequired["capo_datazone.types.updated_by.UpdatedBy"]
    """<p>The Amazon DataZone user who updated the listing.</p>"""
    item: NotRequired["capo_datazone.types.listing_item.ListingItem"]
    """<p>The details of a listing.</p>"""
    name: NotRequired["capo_datazone.types.listing_name.ListingName"]
    """<p>The name of the listing.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description of the listing.</p>"""
    status: NotRequired["capo_datazone.types.listing_status.ListingStatus"]
    """<p>The status of the listing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetListingOutput) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["id"] = value["id"]
    out["listingRevision"] = value["listing_revision"]
    if "created_at" in value:
        import capo_datazone.types.created_at

        out["createdAt"] = capo_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_datazone.types.updated_at

        out["updatedAt"] = capo_datazone.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    if "item" in value:
        import capo_datazone.types.listing_item

        out["item"] = capo_datazone.types.listing_item.serialize_json(value["item"])
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        import capo_datazone.types.listing_status

        out["status"] = capo_datazone.types.listing_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> GetListingOutput:
    out: GetListingOutput = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("GetListingOutput.domain_id required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetListingOutput.id required")
    if "listingRevision" in data:
        out["listing_revision"] = data["listingRevision"]
    else:
        raise DeserializationError("GetListingOutput.listing_revision required")
    if "createdAt" in data:
        import capo_datazone.types.created_at

        out["created_at"] = capo_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if "updatedAt" in data:
        import capo_datazone.types.updated_at

        out["updated_at"] = capo_datazone.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    if "item" in data:
        import capo_datazone.types.listing_item

        out["item"] = capo_datazone.types.listing_item.deserialize_json(data["item"])
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "status" in data:
        import capo_datazone.types.listing_status

        out["status"] = capo_datazone.types.listing_status.deserialize_json(
            data["status"]
        )
    return out
