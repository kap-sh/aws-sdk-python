"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#Entity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_marketplace_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.entity_type
    import capo_marketplace_catalog.types.identifier


class Entity(TypedDict, closed=True):
    type: "capo_marketplace_catalog.types.entity_type.EntityType"
    """<p>The type of entity.</p>"""
    identifier: NotRequired["capo_marketplace_catalog.types.identifier.Identifier"]
    """<p>The identifier for the entity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Entity) -> dict:
    out: dict = {}
    out["Type"] = value["type"]
    if "identifier" in value:
        out["Identifier"] = value["identifier"]
    return out


def deserialize_json(data: dict) -> Entity:
    out: Entity = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    else:
        raise DeserializationError("Entity.type required")
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    return out
