"""Generated from Smithy shape ``com.amazonaws.datazone#CreateListingChangeSetInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.change_action
    import aws_sdk_datazone.types.client_token
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.entity_identifier
    import aws_sdk_datazone.types.entity_type
    import aws_sdk_datazone.types.revision


class CreateListingChangeSetInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain.</p>"""
    entity_identifier: "aws_sdk_datazone.types.entity_identifier.EntityIdentifier"
    """<p>The ID of the asset.</p>"""
    entity_type: "aws_sdk_datazone.types.entity_type.EntityType"
    """<p>The type of an entity.</p>"""
    entity_revision: NotRequired["aws_sdk_datazone.types.revision.Revision"]
    """<p>The revision of an asset.</p>"""
    action: "aws_sdk_datazone.types.change_action.ChangeAction"
    """<p>Specifies whether to publish or unpublish a listing.</p>"""
    client_token: NotRequired["aws_sdk_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateListingChangeSetInput) -> dict:
    out: dict = {}
    out["entityIdentifier"] = value["entity_identifier"]
    import aws_sdk_datazone.types.entity_type

    out["entityType"] = aws_sdk_datazone.types.entity_type.serialize_json(
        value["entity_type"]
    )
    if "entity_revision" in value:
        out["entityRevision"] = value["entity_revision"]
    import aws_sdk_datazone.types.change_action

    out["action"] = aws_sdk_datazone.types.change_action.serialize_json(value["action"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateListingChangeSetInput:
    out: CreateListingChangeSetInput = {}  # type: ignore[typeddict-item]
    if "entityIdentifier" in data:
        out["entity_identifier"] = data["entityIdentifier"]
    else:
        raise DeserializationError(
            "CreateListingChangeSetInput.entity_identifier required"
        )
    if "entityType" in data:
        import aws_sdk_datazone.types.entity_type

        out["entity_type"] = aws_sdk_datazone.types.entity_type.deserialize_json(
            data["entityType"]
        )
    else:
        raise DeserializationError("CreateListingChangeSetInput.entity_type required")
    if "entityRevision" in data:
        out["entity_revision"] = data["entityRevision"]
    if "action" in data:
        import aws_sdk_datazone.types.change_action

        out["action"] = aws_sdk_datazone.types.change_action.deserialize_json(
            data["action"]
        )
    else:
        raise DeserializationError("CreateListingChangeSetInput.action required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
