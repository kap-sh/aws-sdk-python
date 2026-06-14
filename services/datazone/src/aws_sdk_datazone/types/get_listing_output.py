"""Generated from Smithy shape ``com.amazonaws.datazone#GetListingOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.created_at
    import aws_sdk_datazone.types.created_by
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.listing_id
    import aws_sdk_datazone.types.listing_item
    import aws_sdk_datazone.types.listing_name
    import aws_sdk_datazone.types.listing_status
    import aws_sdk_datazone.types.revision
    import aws_sdk_datazone.types.updated_at
    import aws_sdk_datazone.types.updated_by


class GetListingOutput(TypedDict):
    domain_id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain.</p>"""
    id: "aws_sdk_datazone.types.listing_id.ListingId"
    """<p>The ID of the listing.</p>"""
    listing_revision: "aws_sdk_datazone.types.revision.Revision"
    """<p>The revision of a listing.</p>"""
    created_at: NotRequired["aws_sdk_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp of when the listing was created.</p>"""
    updated_at: NotRequired["aws_sdk_datazone.types.updated_at.UpdatedAt"]
    """<p>The timestamp of when the listing was updated.</p>"""
    created_by: NotRequired["aws_sdk_datazone.types.created_by.CreatedBy"]
    """<p>The Amazon DataZone user who created the listing.</p>"""
    updated_by: NotRequired["aws_sdk_datazone.types.updated_by.UpdatedBy"]
    """<p>The Amazon DataZone user who updated the listing.</p>"""
    item: NotRequired["aws_sdk_datazone.types.listing_item.ListingItem"]
    """<p>The details of a listing.</p>"""
    name: NotRequired["aws_sdk_datazone.types.listing_name.ListingName"]
    """<p>The name of the listing.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The description of the listing.</p>"""
    status: NotRequired["aws_sdk_datazone.types.listing_status.ListingStatus"]
    """<p>The status of the listing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetListingOutput) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["id"] = value["id"]
    out["listingRevision"] = value["listing_revision"]
    if "created_at" in value:
        import aws_sdk_datazone.types.created_at

        out["createdAt"] = aws_sdk_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_datazone.types.updated_at

        out["updatedAt"] = aws_sdk_datazone.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    if "item" in value:
        import aws_sdk_datazone.types.listing_item

        out["item"] = aws_sdk_datazone.types.listing_item.serialize_json(value["item"])
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        import aws_sdk_datazone.types.listing_status

        out["status"] = aws_sdk_datazone.types.listing_status.serialize_json(
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
        import aws_sdk_datazone.types.created_at

        out["created_at"] = aws_sdk_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if "updatedAt" in data:
        import aws_sdk_datazone.types.updated_at

        out["updated_at"] = aws_sdk_datazone.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    if "item" in data:
        import aws_sdk_datazone.types.listing_item

        out["item"] = aws_sdk_datazone.types.listing_item.deserialize_json(data["item"])
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "status" in data:
        import aws_sdk_datazone.types.listing_status

        out["status"] = aws_sdk_datazone.types.listing_status.deserialize_json(
            data["status"]
        )
    return out
