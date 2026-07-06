"""Generated from Smithy shape ``com.amazonaws.datazone#AssetInDataProductListingItem``."""

from typing_extensions import NotRequired, TypedDict


class AssetInDataProductListingItem(TypedDict, closed=True):
    entity_id: NotRequired["str"]
    """<p>The entity ID of the listing of the asset in a data product.</p>"""
    entity_revision: NotRequired["str"]
    """<p>The entity revision of the listing of the asset in a data product.</p>"""
    entity_type: NotRequired["str"]
    """<p>The entity type of the listing of the asset in a data product.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetInDataProductListingItem) -> dict:
    out: dict = {}
    if "entity_id" in value:
        out["entityId"] = value["entity_id"]
    if "entity_revision" in value:
        out["entityRevision"] = value["entity_revision"]
    if "entity_type" in value:
        out["entityType"] = value["entity_type"]
    return out


def deserialize_json(data: dict) -> AssetInDataProductListingItem:
    out: AssetInDataProductListingItem = {}  # type: ignore[typeddict-item]
    if "entityId" in data:
        out["entity_id"] = data["entityId"]
    if "entityRevision" in data:
        out["entity_revision"] = data["entityRevision"]
    if "entityType" in data:
        out["entity_type"] = data["entityType"]
    return out
