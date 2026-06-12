"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#EntityRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_marketplace_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.catalog
    import aws_sdk_marketplace_catalog.types.entity_id


class EntityRequest(TypedDict):
    catalog: "aws_sdk_marketplace_catalog.types.catalog.Catalog"
    """<p>The name of the catalog the entity is present in. The only value at this time is <code>AWSMarketplace</code>.</p>"""
    entity_id: "aws_sdk_marketplace_catalog.types.entity_id.EntityId"
    """<p>The ID of the entity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EntityRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["EntityId"] = value["entity_id"]
    return out


def deserialize_json(data: dict) -> EntityRequest:
    out: EntityRequest = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("EntityRequest.catalog required")
    if "EntityId" in data:
        out["entity_id"] = data["EntityId"]
    else:
        raise DeserializationError("EntityRequest.entity_id required")
    return out
