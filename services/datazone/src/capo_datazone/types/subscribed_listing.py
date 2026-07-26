"""Generated from Smithy shape ``com.amazonaws.datazone#SubscribedListing``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.description
    import capo_datazone.types.listing_id
    import capo_datazone.types.listing_name
    import capo_datazone.types.project_id
    import capo_datazone.types.revision
    import capo_datazone.types.subscribed_listing_item


class SubscribedListing(TypedDict, closed=True):
    id: "capo_datazone.types.listing_id.ListingId"
    """<p>The identifier of the published asset for which the subscription grant is created.</p>"""
    revision: NotRequired["capo_datazone.types.revision.Revision"]
    """<p>The revision of the published asset for which the subscription grant is created.</p>"""
    name: "capo_datazone.types.listing_name.ListingName"
    """<p>The name of the published asset for which the subscription grant is created.</p>"""
    description: "capo_datazone.types.description.Description"
    """<p>The description of the published asset for which the subscription grant is created.</p>"""
    item: "capo_datazone.types.subscribed_listing_item.SubscribedListingItem"
    """<p>The published asset for which the subscription grant is created.</p>"""
    owner_project_id: "capo_datazone.types.project_id.ProjectId"
    """<p>The identifier of the project of the published asset for which the subscription grant is created.</p>"""
    owner_project_name: NotRequired["str"]
    """<p>The name of the project that owns the published asset for which the subscription grant is created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubscribedListing) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "revision" in value:
        out["revision"] = value["revision"]
    out["name"] = value["name"]
    out["description"] = value["description"]
    import capo_datazone.types.subscribed_listing_item

    out["item"] = capo_datazone.types.subscribed_listing_item.serialize_json(
        value["item"]
    )
    out["ownerProjectId"] = value["owner_project_id"]
    if "owner_project_name" in value:
        out["ownerProjectName"] = value["owner_project_name"]
    return out


def deserialize_json(data: dict) -> SubscribedListing:
    out: SubscribedListing = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("SubscribedListing.id required")
    if "revision" in data:
        out["revision"] = data["revision"]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("SubscribedListing.name required")
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError("SubscribedListing.description required")
    if "item" in data:
        import capo_datazone.types.subscribed_listing_item

        out["item"] = capo_datazone.types.subscribed_listing_item.deserialize_json(
            data["item"]
        )
    else:
        raise DeserializationError("SubscribedListing.item required")
    if "ownerProjectId" in data:
        out["owner_project_id"] = data["ownerProjectId"]
    else:
        raise DeserializationError("SubscribedListing.owner_project_id required")
    if "ownerProjectName" in data:
        out["owner_project_name"] = data["ownerProjectName"]
    return out
