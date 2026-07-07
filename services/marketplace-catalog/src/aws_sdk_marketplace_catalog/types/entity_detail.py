"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#EntityDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.arn
    import aws_sdk_marketplace_catalog.types.date_time_iso8601
    import aws_sdk_marketplace_catalog.types.entity_type
    import aws_sdk_marketplace_catalog.types.identifier
    import aws_sdk_marketplace_catalog.types.json_document_type


class EntityDetail(TypedDict, closed=True):
    entity_type: NotRequired["aws_sdk_marketplace_catalog.types.entity_type.EntityType"]
    """<p>The entity type of the entity, in the format of <code>EntityType@Version</code>.</p>"""
    entity_arn: NotRequired["aws_sdk_marketplace_catalog.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the entity.</p>"""
    entity_identifier: NotRequired[
        "aws_sdk_marketplace_catalog.types.identifier.Identifier"
    ]
    """<p>The ID of the entity, in the format of <code>EntityId@RevisionId</code>.</p>"""
    last_modified_date: NotRequired[
        "aws_sdk_marketplace_catalog.types.date_time_iso8601.DateTimeISO8601"
    ]
    """<p>The last time the entity was modified.</p>"""
    details_document: NotRequired[
        "aws_sdk_marketplace_catalog.types.json_document_type.JsonDocumentType"
    ]
    """<p>An object that contains all the details of the entity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EntityDetail) -> dict:
    out: dict = {}
    if "entity_type" in value:
        out["EntityType"] = value["entity_type"]
    if "entity_arn" in value:
        out["EntityArn"] = value["entity_arn"]
    if "entity_identifier" in value:
        out["EntityIdentifier"] = value["entity_identifier"]
    if "last_modified_date" in value:
        out["LastModifiedDate"] = value["last_modified_date"]
    if "details_document" in value:
        out["DetailsDocument"] = value["details_document"]
    return out


def deserialize_json(data: dict) -> EntityDetail:
    out: EntityDetail = {}  # type: ignore[typeddict-item]
    if "EntityType" in data:
        out["entity_type"] = data["EntityType"]
    if "EntityArn" in data:
        out["entity_arn"] = data["EntityArn"]
    if "EntityIdentifier" in data:
        out["entity_identifier"] = data["EntityIdentifier"]
    if "LastModifiedDate" in data:
        out["last_modified_date"] = data["LastModifiedDate"]
    if "DetailsDocument" in data:
        out["details_document"] = data["DetailsDocument"]
    return out
