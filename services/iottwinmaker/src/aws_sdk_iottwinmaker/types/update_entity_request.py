"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#UpdateEntityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.component_updates_map_request
    import aws_sdk_iottwinmaker.types.composite_component_updates_map_request
    import aws_sdk_iottwinmaker.types.description
    import aws_sdk_iottwinmaker.types.entity_id
    import aws_sdk_iottwinmaker.types.entity_name
    import aws_sdk_iottwinmaker.types.id
    import aws_sdk_iottwinmaker.types.parent_entity_update_request


class UpdateEntityRequest(TypedDict, closed=True):
    workspace_id: "aws_sdk_iottwinmaker.types.id.Id"
    """<p>The ID of the workspace that contains the entity.</p>"""
    entity_id: "aws_sdk_iottwinmaker.types.entity_id.EntityId"
    """<p>The ID of the entity.</p>"""
    entity_name: NotRequired["aws_sdk_iottwinmaker.types.entity_name.EntityName"]
    """<p>The name of the entity.</p>"""
    description: NotRequired["aws_sdk_iottwinmaker.types.description.Description"]
    """<p>The description of the entity.</p>"""
    component_updates: NotRequired[
        "aws_sdk_iottwinmaker.types.component_updates_map_request.ComponentUpdatesMapRequest"
    ]
    """<p>An object that maps strings to the component updates in the request. Each string in the mapping must be unique to this object.</p>"""
    composite_component_updates: NotRequired[
        "aws_sdk_iottwinmaker.types.composite_component_updates_map_request.CompositeComponentUpdatesMapRequest"
    ]
    """<p>This is an object that maps strings to <code>compositeComponent</code> updates in the request. Each key of the map represents the <code>componentPath</code> of the <code>compositeComponent</code>.</p>"""
    parent_entity_update: NotRequired[
        "aws_sdk_iottwinmaker.types.parent_entity_update_request.ParentEntityUpdateRequest"
    ]
    """<p>An object that describes the update request for a parent entity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEntityRequest) -> dict:
    out: dict = {}
    if "entity_name" in value:
        out["entityName"] = value["entity_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "component_updates" in value:
        import aws_sdk_iottwinmaker.types.component_updates_map_request

        out["componentUpdates"] = (
            aws_sdk_iottwinmaker.types.component_updates_map_request.serialize_json(
                value["component_updates"]
            )
        )
    if "composite_component_updates" in value:
        import aws_sdk_iottwinmaker.types.composite_component_updates_map_request

        out["compositeComponentUpdates"] = (
            aws_sdk_iottwinmaker.types.composite_component_updates_map_request.serialize_json(
                value["composite_component_updates"]
            )
        )
    if "parent_entity_update" in value:
        import aws_sdk_iottwinmaker.types.parent_entity_update_request

        out["parentEntityUpdate"] = (
            aws_sdk_iottwinmaker.types.parent_entity_update_request.serialize_json(
                value["parent_entity_update"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateEntityRequest:
    out: UpdateEntityRequest = {}  # type: ignore[typeddict-item]
    if "entityName" in data:
        out["entity_name"] = data["entityName"]
    if "description" in data:
        out["description"] = data["description"]
    if "componentUpdates" in data:
        import aws_sdk_iottwinmaker.types.component_updates_map_request

        out["component_updates"] = (
            aws_sdk_iottwinmaker.types.component_updates_map_request.deserialize_json(
                data["componentUpdates"]
            )
        )
    if "compositeComponentUpdates" in data:
        import aws_sdk_iottwinmaker.types.composite_component_updates_map_request

        out["composite_component_updates"] = (
            aws_sdk_iottwinmaker.types.composite_component_updates_map_request.deserialize_json(
                data["compositeComponentUpdates"]
            )
        )
    if "parentEntityUpdate" in data:
        import aws_sdk_iottwinmaker.types.parent_entity_update_request

        out["parent_entity_update"] = (
            aws_sdk_iottwinmaker.types.parent_entity_update_request.deserialize_json(
                data["parentEntityUpdate"]
            )
        )
    return out
