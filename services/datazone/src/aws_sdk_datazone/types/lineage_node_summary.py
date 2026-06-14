"""Generated from Smithy shape ``com.amazonaws.datazone#LineageNodeSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_datazone.types.created_at
    import aws_sdk_datazone.types.created_by
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.lineage_node_id
    import aws_sdk_datazone.types.revision
    import aws_sdk_datazone.types.updated_at
    import aws_sdk_datazone.types.updated_by


class LineageNodeSummary(TypedDict):
    domain_id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain of the data lineage node.</p>"""
    name: NotRequired["str"]
    """<p>The name of the data lineage node.</p>"""
    description: NotRequired["str"]
    """<p>The description of the data lineage node.</p>"""
    created_at: NotRequired["aws_sdk_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp at which the data lineage node was created.</p>"""
    created_by: NotRequired["aws_sdk_datazone.types.created_by.CreatedBy"]
    """<p>The user who created the data lineage node.</p>"""
    updated_at: NotRequired["aws_sdk_datazone.types.updated_at.UpdatedAt"]
    """<p>The timestamp at which the data lineage node was updated.</p>"""
    updated_by: NotRequired["aws_sdk_datazone.types.updated_by.UpdatedBy"]
    """<p>The user who updated the data lineage node.</p>"""
    id: "aws_sdk_datazone.types.lineage_node_id.LineageNodeId"
    """<p>The ID of the data lineage node.</p>"""
    type_name: "str"
    """<p>The name of the type of the data lineage node.</p>"""
    type_revision: NotRequired["aws_sdk_datazone.types.revision.Revision"]
    """<p>The type of the revision of the data lineage node.</p>"""
    source_identifier: NotRequired["str"]
    """<p>The alternate ID of the data lineage node.</p>"""
    event_timestamp: NotRequired["datetime.datetime"]
    """<p>The event timestamp of the data lineage node.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LineageNodeSummary) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "created_at" in value:
        import aws_sdk_datazone.types.created_at

        out["createdAt"] = aws_sdk_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "updated_at" in value:
        import aws_sdk_datazone.types.updated_at

        out["updatedAt"] = aws_sdk_datazone.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    out["id"] = value["id"]
    out["typeName"] = value["type_name"]
    if "type_revision" in value:
        out["typeRevision"] = value["type_revision"]
    if "source_identifier" in value:
        out["sourceIdentifier"] = value["source_identifier"]
    if "event_timestamp" in value:
        import aws_sdk_datazone.types._prelude.timestamp

        out["eventTimestamp"] = (
            aws_sdk_datazone.types._prelude.timestamp.serialize_json(
                value["event_timestamp"]
            )
        )
    return out


def deserialize_json(data: dict) -> LineageNodeSummary:
    out: LineageNodeSummary = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("LineageNodeSummary.domain_id required")
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "createdAt" in data:
        import aws_sdk_datazone.types.created_at

        out["created_at"] = aws_sdk_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    if "updatedAt" in data:
        import aws_sdk_datazone.types.updated_at

        out["updated_at"] = aws_sdk_datazone.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("LineageNodeSummary.id required")
    if "typeName" in data:
        out["type_name"] = data["typeName"]
    else:
        raise DeserializationError("LineageNodeSummary.type_name required")
    if "typeRevision" in data:
        out["type_revision"] = data["typeRevision"]
    if "sourceIdentifier" in data:
        out["source_identifier"] = data["sourceIdentifier"]
    if "eventTimestamp" in data:
        import aws_sdk_datazone.types._prelude.timestamp

        out["event_timestamp"] = (
            aws_sdk_datazone.types._prelude.timestamp.deserialize_json(
                data["eventTimestamp"]
            )
        )
    return out
