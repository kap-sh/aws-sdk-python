"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#EntitySummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.boolean
    import aws_sdk_iottwinmaker.types.description
    import aws_sdk_iottwinmaker.types.entity_id
    import aws_sdk_iottwinmaker.types.entity_name
    import aws_sdk_iottwinmaker.types.parent_entity_id
    import aws_sdk_iottwinmaker.types.status
    import aws_sdk_iottwinmaker.types.timestamp
    import aws_sdk_iottwinmaker.types.twin_maker_arn


class EntitySummary(TypedDict):
    entity_id: "aws_sdk_iottwinmaker.types.entity_id.EntityId"
    """<p>The ID of the entity.</p>"""
    entity_name: "aws_sdk_iottwinmaker.types.entity_name.EntityName"
    """<p>The name of the entity.</p>"""
    arn: "aws_sdk_iottwinmaker.types.twin_maker_arn.TwinMakerArn"
    """<p>The ARN of the entity.</p>"""
    parent_entity_id: NotRequired[
        "aws_sdk_iottwinmaker.types.parent_entity_id.ParentEntityId"
    ]
    """<p>The ID of the parent entity.</p>"""
    status: "aws_sdk_iottwinmaker.types.status.Status"
    """<p>The current status of the entity.</p>"""
    description: NotRequired["aws_sdk_iottwinmaker.types.description.Description"]
    """<p>The description of the entity.</p>"""
    has_child_entities: NotRequired["aws_sdk_iottwinmaker.types.boolean.Boolean"]
    """<p>An <b>eventual</b> Boolean value that specifies whether the entity has child entities or not.</p>"""
    creation_date_time: "aws_sdk_iottwinmaker.types.timestamp.Timestamp"
    """<p>The date and time when the entity was created.</p>"""
    update_date_time: "aws_sdk_iottwinmaker.types.timestamp.Timestamp"
    """<p>The last date and time when the entity was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EntitySummary) -> dict:
    out: dict = {}
    out["entityId"] = value["entity_id"]
    out["entityName"] = value["entity_name"]
    out["arn"] = value["arn"]
    if "parent_entity_id" in value:
        out["parentEntityId"] = value["parent_entity_id"]
    import aws_sdk_iottwinmaker.types.status

    out["status"] = aws_sdk_iottwinmaker.types.status.serialize_json(value["status"])
    if "description" in value:
        out["description"] = value["description"]
    if "has_child_entities" in value:
        out["hasChildEntities"] = value["has_child_entities"]
    import aws_sdk_iottwinmaker.types.timestamp

    out["creationDateTime"] = aws_sdk_iottwinmaker.types.timestamp.serialize_json(
        value["creation_date_time"]
    )
    import aws_sdk_iottwinmaker.types.timestamp

    out["updateDateTime"] = aws_sdk_iottwinmaker.types.timestamp.serialize_json(
        value["update_date_time"]
    )
    return out


def deserialize_json(data: dict) -> EntitySummary:
    out: EntitySummary = {}  # type: ignore[typeddict-item]
    if "entityId" in data:
        out["entity_id"] = data["entityId"]
    else:
        raise DeserializationError("EntitySummary.entity_id required")
    if "entityName" in data:
        out["entity_name"] = data["entityName"]
    else:
        raise DeserializationError("EntitySummary.entity_name required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("EntitySummary.arn required")
    if "parentEntityId" in data:
        out["parent_entity_id"] = data["parentEntityId"]
    if "status" in data:
        import aws_sdk_iottwinmaker.types.status

        out["status"] = aws_sdk_iottwinmaker.types.status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("EntitySummary.status required")
    if "description" in data:
        out["description"] = data["description"]
    if "hasChildEntities" in data:
        out["has_child_entities"] = data["hasChildEntities"]
    if "creationDateTime" in data:
        import aws_sdk_iottwinmaker.types.timestamp

        out["creation_date_time"] = (
            aws_sdk_iottwinmaker.types.timestamp.deserialize_json(
                data["creationDateTime"]
            )
        )
    else:
        raise DeserializationError("EntitySummary.creation_date_time required")
    if "updateDateTime" in data:
        import aws_sdk_iottwinmaker.types.timestamp

        out["update_date_time"] = aws_sdk_iottwinmaker.types.timestamp.deserialize_json(
            data["updateDateTime"]
        )
    else:
        raise DeserializationError("EntitySummary.update_date_time required")
    return out
