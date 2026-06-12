"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#GetEntityResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.boolean
    import aws_sdk_iottwinmaker.types.components_map
    import aws_sdk_iottwinmaker.types.description
    import aws_sdk_iottwinmaker.types.entity_id
    import aws_sdk_iottwinmaker.types.entity_name
    import aws_sdk_iottwinmaker.types.id
    import aws_sdk_iottwinmaker.types.parent_entity_id
    import aws_sdk_iottwinmaker.types.status
    import aws_sdk_iottwinmaker.types.sync_source
    import aws_sdk_iottwinmaker.types.timestamp
    import aws_sdk_iottwinmaker.types.twin_maker_arn


class GetEntityResponse(TypedDict):
    entity_id: "aws_sdk_iottwinmaker.types.entity_id.EntityId"
    """<p>The ID of the entity.</p>"""
    entity_name: "aws_sdk_iottwinmaker.types.entity_name.EntityName"
    """<p>The name of the entity.</p>"""
    arn: "aws_sdk_iottwinmaker.types.twin_maker_arn.TwinMakerArn"
    """<p>The ARN of the entity.</p>"""
    status: "aws_sdk_iottwinmaker.types.status.Status"
    """<p>The current status of the entity.</p>"""
    workspace_id: "aws_sdk_iottwinmaker.types.id.Id"
    """<p>The ID of the workspace.</p>"""
    description: NotRequired["aws_sdk_iottwinmaker.types.description.Description"]
    """<p>The description of the entity.</p>"""
    components: NotRequired["aws_sdk_iottwinmaker.types.components_map.ComponentsMap"]
    """<p>An object that maps strings to the components in the entity. Each string in the mapping must be unique to this object.</p>"""
    parent_entity_id: "aws_sdk_iottwinmaker.types.parent_entity_id.ParentEntityId"
    """<p>The ID of the parent entity for this entity.</p>"""
    has_child_entities: "aws_sdk_iottwinmaker.types.boolean.Boolean"
    """<p>A Boolean value that specifies whether the entity has associated child entities.</p>"""
    creation_date_time: "aws_sdk_iottwinmaker.types.timestamp.Timestamp"
    """<p>The date and time when the entity was created.</p>"""
    update_date_time: "aws_sdk_iottwinmaker.types.timestamp.Timestamp"
    """<p>The date and time when the entity was last updated.</p>"""
    sync_source: NotRequired["aws_sdk_iottwinmaker.types.sync_source.SyncSource"]
    """<p>The syncSource of the sync job, if this entity was created by a sync job.</p>"""
    are_all_components_returned: NotRequired[
        "aws_sdk_iottwinmaker.types.boolean.Boolean"
    ]
    """<p>This flag notes whether all components are returned in the API response. The maximum number of components returned is 30.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEntityResponse) -> dict:
    out: dict = {}
    out["entityId"] = value["entity_id"]
    out["entityName"] = value["entity_name"]
    out["arn"] = value["arn"]
    import aws_sdk_iottwinmaker.types.status

    out["status"] = aws_sdk_iottwinmaker.types.status.serialize_json(value["status"])
    out["workspaceId"] = value["workspace_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "components" in value:
        import aws_sdk_iottwinmaker.types.components_map

        out["components"] = aws_sdk_iottwinmaker.types.components_map.serialize_json(
            value["components"]
        )
    out["parentEntityId"] = value["parent_entity_id"]
    out["hasChildEntities"] = value["has_child_entities"]
    import aws_sdk_iottwinmaker.types.timestamp

    out["creationDateTime"] = aws_sdk_iottwinmaker.types.timestamp.serialize_json(
        value["creation_date_time"]
    )
    import aws_sdk_iottwinmaker.types.timestamp

    out["updateDateTime"] = aws_sdk_iottwinmaker.types.timestamp.serialize_json(
        value["update_date_time"]
    )
    if "sync_source" in value:
        out["syncSource"] = value["sync_source"]
    if "are_all_components_returned" in value:
        out["areAllComponentsReturned"] = value["are_all_components_returned"]
    return out


def deserialize_json(data: dict) -> GetEntityResponse:
    out: GetEntityResponse = {}  # type: ignore[typeddict-item]
    if "entityId" in data:
        out["entity_id"] = data["entityId"]
    else:
        raise DeserializationError("GetEntityResponse.entity_id required")
    if "entityName" in data:
        out["entity_name"] = data["entityName"]
    else:
        raise DeserializationError("GetEntityResponse.entity_name required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetEntityResponse.arn required")
    if "status" in data:
        import aws_sdk_iottwinmaker.types.status

        out["status"] = aws_sdk_iottwinmaker.types.status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GetEntityResponse.status required")
    if "workspaceId" in data:
        out["workspace_id"] = data["workspaceId"]
    else:
        raise DeserializationError("GetEntityResponse.workspace_id required")
    if "description" in data:
        out["description"] = data["description"]
    if "components" in data:
        import aws_sdk_iottwinmaker.types.components_map

        out["components"] = aws_sdk_iottwinmaker.types.components_map.deserialize_json(
            data["components"]
        )
    if "parentEntityId" in data:
        out["parent_entity_id"] = data["parentEntityId"]
    else:
        raise DeserializationError("GetEntityResponse.parent_entity_id required")
    if "hasChildEntities" in data:
        out["has_child_entities"] = data["hasChildEntities"]
    else:
        raise DeserializationError("GetEntityResponse.has_child_entities required")
    if "creationDateTime" in data:
        import aws_sdk_iottwinmaker.types.timestamp

        out["creation_date_time"] = (
            aws_sdk_iottwinmaker.types.timestamp.deserialize_json(
                data["creationDateTime"]
            )
        )
    else:
        raise DeserializationError("GetEntityResponse.creation_date_time required")
    if "updateDateTime" in data:
        import aws_sdk_iottwinmaker.types.timestamp

        out["update_date_time"] = aws_sdk_iottwinmaker.types.timestamp.deserialize_json(
            data["updateDateTime"]
        )
    else:
        raise DeserializationError("GetEntityResponse.update_date_time required")
    if "syncSource" in data:
        out["sync_source"] = data["syncSource"]
    if "areAllComponentsReturned" in data:
        out["are_all_components_returned"] = data["areAllComponentsReturned"]
    return out
