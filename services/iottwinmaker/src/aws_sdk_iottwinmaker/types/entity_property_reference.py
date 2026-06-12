"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#EntityPropertyReference``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.component_path
    import aws_sdk_iottwinmaker.types.entity_id
    import aws_sdk_iottwinmaker.types.external_id_property
    import aws_sdk_iottwinmaker.types.name


class EntityPropertyReference(TypedDict):
    component_name: NotRequired["aws_sdk_iottwinmaker.types.name.Name"]
    """<p>The name of the component.</p>"""
    component_path: NotRequired[
        "aws_sdk_iottwinmaker.types.component_path.ComponentPath"
    ]
    """<p>This string specifies the path to the composite component, starting from the top-level component.</p>"""
    external_id_property: NotRequired[
        "aws_sdk_iottwinmaker.types.external_id_property.ExternalIdProperty"
    ]
    """<p>A mapping of external IDs to property names. External IDs uniquely identify properties from external data stores.</p>"""
    entity_id: NotRequired["aws_sdk_iottwinmaker.types.entity_id.EntityId"]
    """<p>The ID of the entity.</p>"""
    property_name: "aws_sdk_iottwinmaker.types.name.Name"
    """<p>The name of the property.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EntityPropertyReference) -> dict:
    out: dict = {}
    if "component_name" in value:
        out["componentName"] = value["component_name"]
    if "component_path" in value:
        out["componentPath"] = value["component_path"]
    if "external_id_property" in value:
        import aws_sdk_iottwinmaker.types.external_id_property

        out["externalIdProperty"] = (
            aws_sdk_iottwinmaker.types.external_id_property.serialize_json(
                value["external_id_property"]
            )
        )
    if "entity_id" in value:
        out["entityId"] = value["entity_id"]
    out["propertyName"] = value["property_name"]
    return out


def deserialize_json(data: dict) -> EntityPropertyReference:
    out: EntityPropertyReference = {}  # type: ignore[typeddict-item]
    if "componentName" in data:
        out["component_name"] = data["componentName"]
    if "componentPath" in data:
        out["component_path"] = data["componentPath"]
    if "externalIdProperty" in data:
        import aws_sdk_iottwinmaker.types.external_id_property

        out["external_id_property"] = (
            aws_sdk_iottwinmaker.types.external_id_property.deserialize_json(
                data["externalIdProperty"]
            )
        )
    if "entityId" in data:
        out["entity_id"] = data["entityId"]
    if "propertyName" in data:
        out["property_name"] = data["propertyName"]
    else:
        raise DeserializationError("EntityPropertyReference.property_name required")
    return out
