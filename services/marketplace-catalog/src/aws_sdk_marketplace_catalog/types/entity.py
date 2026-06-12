"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#Entity``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_marketplace_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.entity_type
    import aws_sdk_marketplace_catalog.types.identifier


class Entity(TypedDict):
    type: "aws_sdk_marketplace_catalog.types.entity_type.EntityType"
    """<p>The type of entity.</p>"""
    identifier: NotRequired["aws_sdk_marketplace_catalog.types.identifier.Identifier"]
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
